#include <gtest/gtest.h>
#include <math.h>



// Demonstrate some basic assertions.
TEST(Add, Point_add_float) {
    Point p(5, 4);
    Point result = Math::add(p, 5.0);
    ASSERT_EQ(result.getX(), 10);
    ASSERT_EQ(result.getY(), 9);
}

TEST(Create, Point_create) {
    Point p(5, 4);
    ASSERT_EQ(p.getX(), 5);
    ASSERT_EQ(p.getY(), 4);
}

TEST(Vector, Vector_create) {
    Vector v(5, 4);
    ASSERT_EQ(v.getX(), 5);
    ASSERT_EQ(v.getY(), 4);
}
