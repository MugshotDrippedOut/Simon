#ifndef VECTOR_H
#define VECTOR_H

template <class T>
class Vector {
private:
    T _x;
public:
    Vector(T x);
    T getX() const;
};

template <class T>
std::ostream& operator<<(std::ostream& os, const Vector<T>& vec);

#include "../template/vector.tpp"

#endif // VECTOR_H