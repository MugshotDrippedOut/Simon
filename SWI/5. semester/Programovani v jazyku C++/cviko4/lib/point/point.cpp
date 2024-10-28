#include <point.h>

Point::Point(float x, float y)
{
    _x = x;
    _y = y;
}

float Point::getX()
{
    return _x;
}

float Point::getY()
{
    return _y;
}

void Point::print()
{
    std::cout << _x << "," << _y << std::endl;
}

float Point::add(float a, float b)
{
    return a + b;
}

Point Point::add(Point p, float num)
{
    return Point(p.getX() + num, p.getY() + num);
}
