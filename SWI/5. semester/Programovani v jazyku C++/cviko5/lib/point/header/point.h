template<class T>
class Point {
    private:
        T _x;
    public:
        Point(T x) : _x(x) {}
        T getX() const ;

        void print() const ;

};

#include "../template/point.tpp"