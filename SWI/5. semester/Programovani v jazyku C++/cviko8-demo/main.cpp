/*
Minule jsme si vytvořili templatovaný Point a Vektor.

Dnes je vylepšíme o koncepty:
- přidej koncept, který zamezí substituci T za něco co by se nedalo sčítat
- pak demonstruj sečtení dvou čísel pomocí součtu Point<int> + Vektor<int>
- pak demonstruj koncepty tak, že se pokusíš sečíst Point<TřidaBez+> + Vektor<Trida> (tyto třídy stačí mít v main.cpp)
- nakonec vytvoř dvě třídy (stačí v main.cpp, případně test.cpp)

**Pro pondělní hodiny**
- TODO

**Pro úterní hodiny**
- třída Time, která bude reprezentovat bod (Rok, Měsíc, den, hodina, minuta)
- třída Duration, která bude reprezentovat vektor (minuty)
- V mainu demonstruj, jak vytvoříš bod, který obsahuje aktuální čas a přidej k němu různý počet minut
- je nezbytné respektovat přechody! 🕢 + 30m = 🕗
- ([2024 12.11. 7:30] + 30m = [2024 12.11. 8:00]),
- ([2024 12.11. 23:40] + 40m = [2024 13.11. 00:20])
- každý měsíc má 30 dnů, rok má 12 měsíců

- testy jsou za bod navíc
*/
#include <iostream>
#include <optional>
#include <concepts>

template <typename T>
concept Addable = requires(T a, T b) {
    { a + b } -> std::convertible_to<T>;
};



template <Addable T>
T add(T a, T b) {
    return a + b;
}

template <typename T>
class Vektor {
private:
    T _x;
public:
    Vektor(T x) : _x(x) {}

    T getX() const {
        return _x;
    }


    friend std::ostream& operator<<(std::ostream& os, const Vektor& vektor) {
        os << "Vektor(" << vektor.getX() << ")";
        return os;
    }
};

template <typename T>
class Point {
private:
    T _x;
public:
    Point(T x) : _x(x) {}

    T getX() const {
        return _x;
    }

    Point<T> operator+(const Vektor<T>& vektor) {
        return Point<T>(_x + vektor.getX());
    }
    Vektor<T> operator-(const Point<T>& other) {
        return Vektor<T>(_x - other.getX());
    }
    friend std::ostream& operator<<(std::ostream& os, const Point& point) {
        os << "Point(" << point.getX() << ")";
        return os;
    }

};


template <typename T>
class Duration {
private:
    T _minutes;
public:
    Duration(T minutes) : _minutes(minutes) {}

    T getMinutes() const {
        return _minutes;
    }

    friend std::ostream& operator<<(std::ostream& os, const Duration& duration) {
        os << "Duration(" << duration.getMinutes() << ")";
        return os;
    }
};


template <typename T>
class Time {  // Rok, den, měsíc, hodina, minuta
private:
    T _year;
    T _day;
    T _month;
    T _hour;
    T _minute;
public: 
    Time(T year, T day, T month, T hour, T minute) : _year(year), _day(day), _month(month), _hour(hour), _minute(minute) {}

    T getYear() const {
        return _year;
    }

    T getMonth() const {
        return _month;
    }

    T getDay() const {
        return _day;
    }

    T getHour() const {
        return _hour;
    }

    T getMinute() const {
        return _minute;
    }

    Time<T> operator+(const Duration<T>& duration) {
        T minutes = add(_minute, duration.getMinutes());
        T hours = _hour + minutes / 60;
        minutes %= 60;
        T days = _day + hours / 24;
        hours %= 24;
        T months = _month;
        T years = _year;
        while (days > 30) {
            days -= 30;
            months++;
            if (months > 12) {
                months = 1;
                years++;
            }
        }
        return Time<T>(years, days, months, hours, minutes);
    }

    Duration<T> operator-(const Time<T>& other) {
        T minutes = (_year - other.getYear()) * 12 * 30 * 24 * 60 + (_month - other.getMonth()) * 30 * 24 * 60 + (_day - other.getDay()) * 24 * 60 + (_hour - other.getHour()) * 60 + (_minute - other.getMinute());
        return Duration<T>(minutes);
    }

    friend std::ostream& operator<<(std::ostream& os, const Time& time) {
        os << "Time(" << time.getYear() << " " << time.getMonth() << "." << time.getDay() << " " << time.getHour() << ":" << time.getMinute() << ")";
        return os;
    }
};




int main() {
    Point<float> point1(5.2f);
    Point<float> point2(10.3f);
    Vektor<float> vektor(5.3f);

    const Point<float> result = point1 + vektor;
    const Vektor<float> result2 = point1 - point2;


    std::cout << result << std::endl;
    std::cout << vektor << std::endl;

    std::cout << result2 << std::endl;

    Time<int> time(2024, 12, 11, 7, 30);
    Duration<int> duration(3);

    std::cout << time << std::endl;

    Time<int> newTime = time + duration;

    std::cout << newTime << std::endl;

    return 0;
}