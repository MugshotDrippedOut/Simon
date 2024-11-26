#include <gtest/gtest.h>
#include <iostream>
#include <point.h>
#include "vector.h"


TEST(Create, Point_create){
    Point p(5.5f);
    ASSERT_EQ(p.getX(), 5.5f);
}

TEST(Create, Point_vector){
    Vector v(2.2f);
    ASSERT_EQ(v.getX(), 2.2f);
}

TEST(ADD, Add_vector_to_point){
    Point p(5.5f);
    Vector v(2.2f);

    const Point<float> np = p + v;
    ASSERT_EQ(np.getX(), 7.7f);
}

TEST(SUBTRACK, Subtruck_point_from_point){
    Point p1(5.5f);
    Point p2(2.2f);

    const Vector<float> nv = p1 - p2 ;
    ASSERT_EQ(nv.getX(), 3.3f);
}

TEST(STREAM, Stream_operator_point){
    Point p(5.5f);
    std::stringstream out;
    out <<p;
    ASSERT_EQ(out.str(), "Point(5.5)");
}

TEST(STREAM, Stream_operator_vector){
    Vector v(2.2f);
    std::stringstream out;
    out <<v;
    ASSERT_EQ(out.str(), "Vector(2.2)");
}

