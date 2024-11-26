#include <iostream>
#include <concepts>

template <class T>
Point<T>::Point(T x) : _x(x) {}

template <class T>
T Point<T>::getX() const {
    return _x;
}

template <class T>
    template <typename S> requires Addable<T, S>
Point<T> Point<T>::operator+(const Vector<S>& vec) const {
    return Point<T>(_x+ vec.getX());
}
template <class T>
Vector<T> Point<T>::operator-(const Point<T>& p) const {
    return Vector<T>(_x - p.getX());
}

template <class T>
std::ostream& operator<<(std::ostream& os, const Point<T>& point) {
    os << "Point(" << point.getX() << ")";
    return os;
}