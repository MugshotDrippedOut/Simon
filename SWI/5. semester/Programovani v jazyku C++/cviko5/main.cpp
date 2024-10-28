#include <iostream>

class TwoD
{
    private:
        float _x, _y;

    public:
        TwoD (float x, float y) : _x(x), _y(y) {}
        friend std::ostream& operator << (std::ostream &os, const TwoD &dt);

};

std::ostream&operator << (std::ostream &os, const TwoD &dt) {
    os << "2D(" << dt._x << ", " << dt._y << ")";
    return os;
}






int main() {

    const TwoD p(1.0, 2.0);
    std::cout << p << std::endl;

    const Point <TwoD> p1(TwoD(1.5f, 2.3f));
    p1.print();

    return 0;
}