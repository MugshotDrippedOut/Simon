#include <iostream>

template <class T>
Vector<T>::Vector(T x) : _x(x) {}

template <class T>
T Vector<T>::getX() const {
    return _x;
}

template <class T>
std::ostream& operator<<(std::ostream& os, const Vector<T>& vec) {
    os << "Vector(" << vec.getX() << ")";
    return os;
}

