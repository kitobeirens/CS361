{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kitobeirens/CS361/blob/master/FinalHomework.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "metadata": {
        "id": "z_GsmfFPWT_L",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1389
        },
        "outputId": "081f77d4-88ac-4f30-d76e-65133021a012"
      },
      "cell_type": "code",
      "source": [
        "# -*- coding: utf-8 -*-\n",
        "\"\"\"Untitled1.ipynb\n",
        "\n",
        "Automatically generated by Colaboratory.\n",
        "\n",
        "Original file is located at\n",
        "    https://colab.research.google.com/drive/1fq_gWAAYJIWwoIqxWINzHJVrjBH5QXCu\n",
        "\"\"\"\n",
        "\n",
        "#1a: prints the result as a double because the result is a fraction 1.666667\n",
        "#1b: prints the remainder after the modulus is calculated 2\n",
        "#1c: prints the result as a double because the result is a fraction 1.6666667\n",
        "#1d: prints the result as a double because the result is a fraction 1.666667\n",
        "#1e:  prints the remainder after the modulus is calculated, which is 2.2\n",
        "\n",
        "#2a: Can not print out as it has too many digits so there is a stack overflow error\n",
        "#2b: prints 1.0 as it calculates the equation as a double\n",
        "#2c: prints 0.0 because rounding occurs due to the very high numbers\n",
        "\n",
        "#3a: Converts from int to a float 123.0\n",
        "#3b: converts from a string to a float 123.0\n",
        "#3c: converts from a string to a float 123.23\n",
        "#3d: converts from a float to an int and round down 123\n",
        "#3e: cannot be converted from a string to int as it is in decimal form\n",
        "#3f: converst to a float from a string and then to an int so this works\n",
        "#3g: converts an int to a string\n",
        "#3h: converts a float to a string\n",
        "#3i: a is converted to true \n",
        "#3j: 0 is converted to false\n",
        "#3k: 0.1 is converted to true because it isnt 0\n",
        "\n",
        "#4: range goes through all values in the specified range, if no first value is given it is assumed 0\n",
        "#4: for i in range(5) will iterate through all of the values 0-5 inclusive. Range is its own class\n",
        "\n",
        "\n",
        "#5\n",
        "numFound = 0\n",
        "x = 11\n",
        "while(numFound < 20):\n",
        "  if(x % 5 == 0 and x % 7 == 0 and x % 11 == 0):\n",
        "    print(x)\n",
        "    numFound+=1\n",
        "  x+=1\n",
        "  \n",
        "#6  \n",
        "import math\n",
        "\n",
        "def is_prime(n):\n",
        "  if n > 1:\n",
        "    for i in range(2, n):\n",
        "      if (n % i) == 0:\n",
        "        return False\n",
        "      else:\n",
        "        return True\n",
        "  else:\n",
        "    return False\n",
        "def form(n):\n",
        "  if((((n - 1)/6)%1) == 0):\n",
        "    return True\n",
        "  elif((((n + 1)/6)%1) == 0):\n",
        "    return True\n",
        "  else:\n",
        "    return False\n",
        "\n",
        "def is_prime(n):\n",
        "  if n > 1:\n",
        "    if(form(n) == True):\n",
        "      for i in range(2, n):\n",
        "        if (n % i) == 0:\n",
        "          return False\n",
        "        else:\n",
        "          return True\n",
        "    else:\n",
        "      return False\n",
        "  else:\n",
        "    return False\n",
        "\n",
        "def all_primes(n):\n",
        "  primeNums = []\n",
        "  for maybe_prime in range(2, n + 1):\n",
        "    isPrime = True\n",
        "    for i in range(2, maybe_prime):\n",
        "      if ((maybe_prime % i) == 0):\n",
        "        isPrime = False\n",
        "    if isPrime:\n",
        "      primeNums.append(maybe_prime)\n",
        "\n",
        "  return(primeNums)\n",
        "\n",
        "print(all_primes(20))\n",
        "\n",
        "def firstPrimes(n):\n",
        "  num = 2\n",
        "  count = 0\n",
        "  while(count != n):\n",
        "    if(is_prime(num)):\n",
        "      print(num)\n",
        "      count+=1\n",
        "    num+=1\n",
        "\n",
        "firstPrimes(10)\n",
        "\n",
        "#7   \n",
        "def printList(list):\n",
        "  for i in list:\n",
        "    print(i)\n",
        "    \n",
        "def printReverse(list):\n",
        "  list.reverse()\n",
        "  for i in list:\n",
        "    print(i)\n",
        "    \n",
        "def lengthOfList(list):\n",
        "  counter = 0\n",
        "  for i in list:\n",
        "    counter+=1\n",
        "  print(counter)\n",
        "  \n",
        "#8  \n",
        "a = [1,2,3,4]\n",
        "b=a\n",
        "b[1] = 5\n",
        "# changing the value of b changes a aswell because it is pass by reference\n",
        "c = a[:]\n",
        "# a[:] creates a copy of the list instead and passes it by value\n",
        "c[2] = 10\n",
        "\n",
        "def set_first_elem_to_zero(list):\n",
        "  list[0] = 0\n",
        "  return list\n",
        "\n",
        "#the function causes the list to be changed permanently\n",
        "\n",
        "print(a)\n",
        "print(set_first_elem_to_zero(a))\n",
        "print(a)\n",
        "\n",
        "def flattenList(list):\n",
        "  flatList = []\n",
        "  for sublist in list:\n",
        "      for val in sublist:\n",
        "          flatList.append(val)\n",
        "  return flatList  \n",
        "\n",
        "#9\n",
        "a = [[1,3], [3,6]]\n",
        "print(flattenList(a))\n",
        "#10\n",
        "import matplotlib.pyplot as plt\n",
        "x = []\n",
        "y = []\n",
        "for i in range(3):\n",
        "  e = ((math.sin(i-2)**2)*(math.e**(-i**2)))\n",
        "  y.append(e)\n",
        "  x.append(i)\n",
        "print(x)\n",
        "print(y)\n",
        "plt.plot(x, y, color=\"red\")\n",
        "plt.title(\"F(x)=sin^2(x-2)e^(-x^2)\")\n",
        "plt.xlabel('X-Axis')\n",
        "plt.ylabel('Y-Axis')\n",
        "plt.show()\n",
        "\n",
        "#11\n",
        "def listIter(list):\n",
        "  total = None\n",
        "  for i in list:\n",
        "    if total is None:\n",
        "      total = i\n",
        "    else:\n",
        "      total = total * int(i)\n",
        "  print(total)\n",
        "  \n",
        "  \n",
        "listIter([5,8,10])\n",
        "\n",
        "def listRecursive(list):\n",
        "  if len(list)==1:\n",
        "        return list[0]\n",
        "  return listRecursive([list[0]]) * listRecursive(list[1:])\n",
        "    \n",
        "a = [1,2,3,4,10]\n",
        "print(listRecursive(a))\n",
        "#12\n",
        "\n",
        "def fib(n):\n",
        "    if n > 1:\n",
        "        return fib(n-1) + fib(n-2)\n",
        "    return n\n",
        "\n",
        "print(fib(6))\n",
        "\n",
        "#13\n",
        "import re\n",
        "#add file name in here!!!!\n",
        "def findEmail():\n",
        "  in_file = open(r\"\",\"rt\")\n",
        "  for line in in_file:\n",
        "    if re.match(r'[\\w\\.-]+@[\\w\\.-]+', line):\n",
        "        print(line)\n",
        "findEmail()\n"
      ],
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "385\n",
            "770\n",
            "1155\n",
            "1540\n",
            "1925\n",
            "2310\n",
            "2695\n",
            "3080\n",
            "3465\n",
            "3850\n",
            "4235\n",
            "4620\n",
            "5005\n",
            "5390\n",
            "5775\n",
            "6160\n",
            "6545\n",
            "6930\n",
            "7315\n",
            "7700\n",
            "[2, 3, 5, 7, 11, 13, 17, 19]\n",
            "5\n",
            "7\n",
            "11\n",
            "13\n",
            "17\n",
            "19\n",
            "23\n",
            "25\n",
            "29\n",
            "31\n",
            "[1, 5, 3, 4]\n",
            "[0, 5, 3, 4]\n",
            "[0, 5, 3, 4]\n",
            "[1, 3, 3, 6]\n",
            "[0, 1, 2]\n",
            "[0.826821810431806, 0.2604856534228343, 0.0]\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<matplotlib.figure.Figure at 0x7fe409ee9c88>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "stream",
          "text": [
            "400\n",
            "240\n",
            "8\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "error",
          "ename": "FileNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-30-9879e87d9298>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m    198\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mre\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmatch\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mr'[\\w\\.-]+@[\\w\\.-]+'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mline\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    199\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mline\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 200\u001b[0;31m \u001b[0mfindEmail\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-30-9879e87d9298>\u001b[0m in \u001b[0;36mfindEmail\u001b[0;34m()\u001b[0m\n\u001b[1;32m    194\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    195\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mfindEmail\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 196\u001b[0;31m   \u001b[0min_file\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mr\"\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"rt\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    197\u001b[0m   \u001b[0;32mfor\u001b[0m \u001b[0mline\u001b[0m \u001b[0;32min\u001b[0m \u001b[0min_file\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    198\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mre\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmatch\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mr'[\\w\\.-]+@[\\w\\.-]+'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mline\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: ''"
          ]
        }
      ]
    }
  ]
}