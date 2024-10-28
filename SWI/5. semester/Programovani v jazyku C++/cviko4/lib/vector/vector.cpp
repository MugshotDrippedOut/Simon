#include <vector.h>

Vector::Vector(float x, float y)
{
    _x = x;
    _y = y;
}

float Vector::getX()
{
    return _x;
}

float Vector::getY()
{
    return _y;
}

void Vector::print()
{
    std::cout << "Vector(" << _x << ", " << _y << ")" << std::endl;
}
