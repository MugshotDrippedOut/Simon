#include <iostream>
#include <list>
#include <memory>

using namespace std;

template<typename T>
concept Scalable = requires(T obj, double scale) {
    {obj * scale} -> std::convertible_to<T>;
};

template<Scalable T>
class ObecnyObjekt {
    public:
    virtual ~ObecnyObjekt() = default; // virtual destructor
    virtual void show () const= 0;        // pure virtual function
    virtual std::shared_ptr<ObecnyObjekt> scale(double scale) const = 0;  
    virtual T getArea() const = 0;
    // Virtual - a function that is declared within a base class and is re-defined(Overriden) by a derived class.
    // default - The default keyword is used to declare a default constructor, a default destructor, a default assignment operator, and a default copy constructor.
};

template<Scalable T>
class Kruh: public ObecnyObjekt<T> {
    private:
        T _r;
    public :
        Kruh(T r) : _r(r) {}
        void show() const override {
            cout << "Kruh" << endl;
        }

        std::shared_ptr<ObecnyObjekt> scale(double scale) const override {
            return std::make_shared<Kruh>(_r * scale);
        }

        float getArea() const override{
            return 3.1415 * _r * _r;
        }
};


class Ctverec: public ObecnyObjekt {
    private:
    float _a;

    public:
    Ctverec(float a ) : _a(a) {} 
    void show() const override{
        cout << "Ctverec" << endl;
    }

    std::shared_ptr<ObecnyObjekt> scale(double scale) const override {
        return std::make_shared<Ctverec>(_a * scale);
    }

    float getArea() const override {
        return _a * _a;
    }

};


int main() {
    std::shared_ptr<ObecnyObjekt> oo = std::make_shared<Ctverec>(Ctverec(20));
    oo->show();
    cout << "Area: " << oo->getArea() << endl;

    list<std::shared_ptr<ObecnyObjekt>> objects;
    objects.push_back(std::make_shared<Ctverec>(Ctverec(2)));
    objects.push_back(std::make_shared<Kruh>(Kruh(3)));

    for (auto o : objects) {
        o->show();
        cout << "Area: " << o->getArea() << endl;
    }
}
