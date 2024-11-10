#ifndef POINT_H
#define POINT_H

#include "vector.h"

template <class T>
class Point {
private:
    T _x;
public:
    Point(T x);
    T getX() const;
    Point<T> operator+(const Vector<T>& vec) const;
    Vector<T> operator-(const Point<T>& p) const;
};

template <class T>
std::ostream& operator<<(std::ostream& os, const Point<T>& point);

#include "../template/point.tpp"

#endif // POINT_H