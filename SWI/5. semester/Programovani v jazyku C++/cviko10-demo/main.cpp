#include <iostream>
#include <vector>
#include <memory>
#include <algorithm>
#include <array>
#include <cmath>


using namespace std;

template <class T>
concept Scalable = requires(T a, double scalar) {
    { a *scalar } -> std::convertible_to<T>;
};


template <Scalable T>
class Vehicle{
    public:
        virtual ~Vehicle() = default;
        virtual void print() const = 0;
        virtual void printVehicleType() const = 0;

        virtual T computeMaxSpeed() const = 0; 
        virtual T estimateTravelTime(T distance) const{
            return (distance / computeMaxSpeed()) * 60;
        }
        /*
        Metoda estimateTravelTime:
            Vypočítá čas potřebný k ujetí zadané vzdálenosti (distance) 
            na základě výsledku computeMaxSpeed.
            Čas je v minutách.
        */





};

template <Scalable T>
class Car : public Vehicle<T>{
    private:
        T _engineSize; //1.0 - 5.0.
        int _seats;
    public:
        Car(T engineSize, int seats) : _engineSize(engineSize), _seats(seats) {}
        void print() const override {
            cout << "Car with engine size: " << _engineSize << " and seats: " << _seats << endl;
        }
        void printVehicleType() const override {
            cout << "Car";
        }
        T computeMaxSpeed() const override {
            return _engineSize * 50 - _seats * 5;
        }


};

template <Scalable T>
class Motorcycle : public Vehicle<T>{
    private:
        T _aerodynamics; //Aerodynamický koeficient (nižší hodnota = lepší aerodynamika).
        int type; // (např. 0 - "sport", 1 - "touring").
    public:
        Motorcycle(T aerodynamics, int type) : _aerodynamics(aerodynamics), type(type) {}
        void print() const override {
            cout << "Motorcycle with aerodynamics: " << _aerodynamics << " and type: " << type << endl;
        }
        void printVehicleType() const override {
            cout << "Motorcycle";
        }
        T computeMaxSpeed() const override {
            if (type == 0) {
                return 200/_aerodynamics;
            } else if (type == 1) {
                return 150/_aerodynamics;
            }
            return 0;
        }



};

template <Scalable T>
class Truck : public Vehicle<T>{
    private:
        T _loadCapacity; //Nosnost v tunách.
        T _engineSize;  // 6.0 - 18.0.
        int _wheelPairs; //Počet párů kol. (2-10).

    public:
        Truck(T loadCapacity, T engineSize, int wheelPairs) 
            : _loadCapacity(loadCapacity), _engineSize(engineSize), _wheelPairs(wheelPairs) {
                _loadCapacity = _loadCapacity < 0 ? 0 : _loadCapacity;  // Nosnost nesmí být záporná.
                _engineSize = _engineSize < 6.0 ? 6.0 : _engineSize;    // Motor nesmí být menší než 6.0.
                _wheelPairs = _wheelPairs < 2 ? 2 : _wheelPairs;        // Počet párů kol nesmí být menší než 2.
            }        
        void print() const override {
            cout << "Truck with load capacity: " << _loadCapacity << " tons || Engine size: " << _engineSize << " || Wheel pairs: " << _wheelPairs << endl;
        }
        void printVehicleType() const override {
            cout << "Truck";
        }
        T computeMaxSpeed() const override {

            T maxSpeed = _engineSize * 40 - (_loadCapacity * 12)/_wheelPairs;
            // Air resistance Based on the load capacity and max speed.  Fd = 0.5 * p * v^2 * Cd * A
            T airResistance = 0.01 * _loadCapacity * pow(maxSpeed, 1.1);
            maxSpeed = maxSpeed - airResistance;

            maxSpeed = maxSpeed < 0 ? 0 : maxSpeed;
            return maxSpeed;
        }
 

};





int main() {

    std::vector<std::unique_ptr<Vehicle<float>>> vehicles;

    vehicles.push_back(std::make_unique<Car<float>>(2.0, 5));
    vehicles.push_back(std::make_unique<Motorcycle<float>>(0.5, 0));
    vehicles.push_back(std::make_unique<Car<float>>(3.0, 4));
    vehicles.push_back(std::make_unique<Motorcycle<float>>(0.8, 1));
    vehicles.push_back(std::make_unique<Truck<float>>(50.0, 7.0, 4));
    vehicles.push_back(std::make_unique<Truck<float>>(20.0, 18.0, 6));
    vehicles.push_back(std::make_unique<Truck<float>>(10.0, 6.0, 2));
    vehicles.push_back(std::make_unique<Motorcycle<float>>(0.7, 0));
    vehicles.push_back(std::make_unique<Car<float>>(1.5, 4));
    vehicles.push_back(std::make_unique<Car<float>>(4.0, 2));
    vehicles.push_back(std::make_unique<Truck<float>>(30.0, 12.0, 8));
    vehicles.push_back(std::make_unique<Truck<float>>(40.0, 10.0, 6));
    vehicles.push_back(std::make_unique<Motorcycle<float>>(0.6, 1));
    vehicles.push_back(std::make_unique<Car<float>>(2.5, 5));
    vehicles.push_back(std::make_unique<Car<float>>(1.0, 4));
    vehicles.push_back(std::make_unique<Truck<float>>(15.0, 8.0, 4));

    std::sort(vehicles.begin(), vehicles.end(), [](const std::unique_ptr<Vehicle<float>> &a, const std::unique_ptr<Vehicle<float>> &b) {
        return a->computeMaxSpeed() > b->computeMaxSpeed();
    });



    for (const auto &vehicle : vehicles) {
        vehicle->print();
        cout << "Max speed: " << vehicle->computeMaxSpeed() << "km/h" << endl;
        cout << "Travel time for 100 km: " << vehicle->estimateTravelTime(100) << " minutes" << endl<<endl;
    }


    int i = 1;
    for (const auto &vehicle : vehicles) {

        vehicle->printVehicleType();
        cout << " " << i << " place => has max speed: " << vehicle->computeMaxSpeed() << "km/h" << endl;
        i++;
    }

    return 0;
}
