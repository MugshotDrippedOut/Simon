// main.cpp
#include <iostream>
#include "point.h"

class Duration {
    private:
        int minutes;
    public:
        Duration (int minutes){
            this->minutes = minutes;
        };
        int getMinutes() const{
            return minutes;
        };
};
class Time {
    private:
        int hours;
        int minutes;
    public:
        Time (int hours, int minutes){
            this->hours = hours;
            this->minutes = minutes;
        };
        int getTime() const{
            return hours * 60 + minutes;
        };

        Time operator+(const Duration& duration) const{
            return Time(hours, minutes + duration.getMinutes());
        };
};






int main() {
    const Point<Time> pointTime(Time(5, 30));
    const Vector<Duration> vectorDur(Duration(20));

    
    const Point<float> point(5.5f);
    const Vector<float> vector(2.2f);




    const Point<float> newPoint = point + vector;
    const Vector<float> newVec = newPoint - point;

    // std::cout << point << std::endl;    // Výstup: Point(5.5)
    std::cout << "new Point => " << point << " + " << vector  << " = ";
    std::cout << newPoint << std::endl;       // Výstup: Point(7.7)
    // std::cout << vector << std::endl;   // Výstup: Vector(2.2)
    std::cout << "new Vector => " << newPoint << " - " << point << " = " ;
    std::cout << newVec << std::endl;   // Výstup: Vector(2.2)

    return 0;
}