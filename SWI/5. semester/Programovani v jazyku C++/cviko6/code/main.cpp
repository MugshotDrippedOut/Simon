// main.cpp
#include <iostream>
#include "point.h"
#include "vector.h"

int main() {
    const Point<float> point(5.5f);
    const Vector<float> vector(2.2f);

    const Point<float> np = point + vector;
    const Vector<float> newVec = np - point;

    std::cout << point << std::endl;    // Výstup: Point(5.5)
    std::cout << np << std::endl;       // Výstup: Point(7.7)
    std::cout << vector << std::endl;   // Výstup: Vector(2.2)
    std::cout << newVec << std::endl;   // Výstup: Vector(2.2)

    return 0;
}