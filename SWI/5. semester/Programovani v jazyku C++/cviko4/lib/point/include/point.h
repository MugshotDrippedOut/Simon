#include <iostream>


/**
 * @brief A class to represent a point in 2D space
 */
class Point
{
private:
    float _x, _y;

public:

    Point(float x, float y);

    float getX();

    float getY();

    void print();

    float add(float a, float b);

    Point add(Point p, float num);

    Point add(class Vector v);
};
