// main.cpp
/*
Minule jsme si vytvořili templatovaný Point a Vektor.

Dnes je vylepšíme o koncepty:

přidej koncept, který zamezí substituci T za něco co by se nedalo sčítat
pak demonstruj sečtení dvou čísel pomocí součtu Point + Vektor
pak demonstruj koncepty tak, že se pokusíš sečíst Point<TřidaBez+> + Vektor (tyto třídy stačí mít v main.cpp)
nakonec vytvoř dvě třídy (stačí v main.cpp, případně test.cpp)
Bonus:

třída Time, která bude reprezentovat bod (Rok, Měsíc, den, hodina, minuta)

třída Duration, která bude reprezentovat vektor (minuty)

V mainu demonstruj, jak vytvoříš bod, který obsahuje aktuální čas a přidej k němu různý počet minut

je nezbytné respektovat přechody! 🕢 + 30m = 🕗

([2024 12.11. 7:30] + 30m = [2024 12.11. 8:00]),

([2024 12.11. 23:40] + 40m = [2024 13.11. 00:20])

každý měsíc má 30 dnů, rok má 12 měsíců

testy jsou za bod navíc
*/

#include <iostream>
#include "point.h"



class Hours {
private:
    int _hour;
public:
    Hours(int hour) : _hour(hour) {}
    int getHour() const { return _hour; }

    friend std::ostream& operator<<(std::ostream& os, const Hours& hours) {
    os << "Hours(" << hours.getHour() << " hours)";
    return os;
    }
};

class Minutes {
private:
    int _minute;
public:
    Minutes(int minute) : _minute(minute) {}
    int getMinute() const { return _minute; }

    friend std::ostream& operator<<(std::ostream& os, const Minutes& minutes) {
    os << "Minutes(" << minutes.getMinute() << " minutes)";
    return os;
    }
};


class Duration {
private:
    int _minute;
public:
    Duration(int minute) : _minute(minute) {}
    int getMinute() const { return _minute; }

    friend std::ostream& operator<<(std::ostream& os, const Duration& duration) {
    os << "Duration(" << duration.getMinute() << " minutes)";
    return os;
    }
};

class Time {
private:
    int _year;
    int _month;
    int _day;
    int _hour;
    int _minute;
public:
    Time(int year, int day, int month, int hour, int minute) : _year(year), _day(day), _month(month), _hour(hour), _minute(minute) {}


    int getYear() const { return _year; }
    int getMonth() const { return _month; }
    int getDay() const { return _day; }
    int getHour() const { return _hour; }
    int getMinute() const { return _minute; }

    
    Time operator+(const Duration& duration) const {
        int newMinute = _minute + duration.getMinute();
        int newHour = _hour + newMinute / 60;
        newMinute %= 60;
        int newDay = _day + newHour / 24;
        newHour %= 24;
        int newMonth = _month;
        int newYear = _year;
        if (newDay > 30) {
            newDay -= 30;
            newMonth++;
        }
        if (newMonth > 12) {
            newMonth -= 12;
            newYear++;
        }

        return Time(newYear, newDay, newMonth, newHour, newMinute);
    }

    Time operator+(const Minutes& minutes) const {
        int newMinute = _minute + minutes.getMinute();
        int newHour = _hour + newMinute / 60;
        newMinute %= 60;
        int newDay = _day + newHour / 24;
        newHour %= 24;
        int newMonth = _month;
        int newYear = _year;
        if (newDay > 30) {
            newDay -= 30;
            newMonth++;
        }
        if (newMonth > 12) {
            newMonth -= 12;
            newYear++;
        }

        return Time(newYear, newDay, newMonth, newHour, newMinute);
    }

    Time operator+(const Hours& hours) const {
        int newHour = _hour + hours.getHour();
        int newDay = _day + newHour / 24;
        newHour %= 24;
        int newMonth = _month;
        int newYear = _year;
        if (newDay > 30) {
            newDay -= 30;
            newMonth++;
        }
        if (newMonth > 12) {
            newMonth -= 12;
            newYear++;
        }

        return Time(newYear, newDay, newMonth, newHour, _minute);
    }

    
    friend std::ostream& operator<<(std::ostream& os, const Time& time) {
        os << "Time(" << time.getYear() << " " << time.getDay() << "." << time.getMonth() << " " << time.getHour() << ":" << time.getMinute() << ")";
        return os;
    }



};






int main() {
    const Point<float> point(5.5f);
    const Vector<float> vector(2.2f);

    const Point<float> newPoint = point + vector;
    const Vector<float> newVec = newPoint - point;

    // std::cout << "new Point => " << point << " + " << vector  << " = ";
    // std::cout << newPoint << std::endl;       // Výstup: Point(7.7)
    // std::cout << "new Vector => " << newPoint << " - " << point << " = " ;
    // std::cout << newVec << std::endl;   // Výstup: Vector(2.2)

    const Point<Time> timePoint(Time(2024, 11, 12, 7, 30));
    const Vector<Duration> durationVector(Duration(40));

    std::cout << "Time point => " << timePoint << " + " << durationVector << " = ";
    const Point<Time> newTimePoint = timePoint + durationVector;
    std::cout << newTimePoint << std::endl;


    const Point<Time> timePoint2(Time(2024, 11, 12, 23, 40));
    const Vector<Hours> durationVector2(Hours(48));

    std::cout << "Time point => " << timePoint2 << " + " << durationVector2 << " = ";
    const Point<Time> newTimePoint2 = timePoint2 + durationVector2;
    std::cout << newTimePoint2 << std::endl;


    return 0;
}