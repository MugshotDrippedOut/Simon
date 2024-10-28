#include <iostream>

/**
 * @brief A class to represent a vector in 2D space
 */
class Vector
{
private:
    float _x, _y;
public:
    Vector(float x, float y);

    float getX();

    float getY();

    void print();
};
