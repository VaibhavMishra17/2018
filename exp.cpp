#include <iostream>
#include <map>

int main()
{

    while (true)
    {

        std::string s1{};
        std::string s2{};

        std::cout << "Enter input:" << std::endl;
        std::cout << "-> ";
        std::cin >> s1;

        if (s1 == "exit")
        {
            break;
        }

        std::cout << "-> ";
        std::cin >> s2;

        std::map<std::string, std::string> mp;

        int i1{}, i2{};

        std::string p1{}, p2{};
        while (s1[i1] != '(')
        {
            p1 += s1[i1];
            i1++;
        }
        i1++;
        while (s2[i2] != '(')
        {
            p2 += s2[i2];
            i2++;
        }
        i2++;

        while (i1 < s1.length() && i2 < s2.length())
        {
            std::string args1{}, args2{};
            while (s1[i1] != ')' && s1[i1] != ',')
            {
                args1 += s1[i1];
                i1++;
            }
            while (s2[i2] != ')' && s2[i2] != ',')
            {
                args2 += s2[i2];
                i2++;
            }

            mp[args1] = args2;
            i1++;
            i2++;
        }

        if (p1 != p2)
        {
            std::cout << "Predicate not same" << std::endl;
        }
        else if (s1[i1 - 1] != s2[i2 - 1])
        {
            std::cout << "Number of arguments not same" << std::endl;
        }
        else
        {
            for (auto i : mp)
            {
                if (i.first == i.second)
                {
                    std::cout << "Substitution not needed" << std::endl;
                }
                else
                {
                    std::cout << "{ " + i.first + "/" + i.second + " }" << std::endl;
                }
            }
        }
    }

    return 0;
}