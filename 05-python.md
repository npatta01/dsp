# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

[![Think Python](img/think_python.png)](http://www.greenteapress.com/thinkpython/)

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

Complete the following exercises to check your ability with Python.

These exercises are implemented with doctests, which are runnable tests inside docstrings. Fill in the function definitions. Correct solutions will make it possible to run (for example) `python -m doctest strings.py` with no messages about failures.

 * [Strings](python/strings.py)
 * [Lists](python/lists.py)


---

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

tuples and list can contain multiple elements.
However, tuples are immutable (so can't add/remove elements)

Keys in  a dictionary need to be immutable, so tuples can be used 


---


---

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets can be used to store multiple elements. 
They differ in that lists allow duplicates unlike sets.

Lets, say you have the 4 numbers, 1,1,2,3....
If you add them to the list, the list will keep all elements
If you add them to a set, the set will only have 3 elements

Finding if an element exists in a set is  O(1) vs O(n) in a list.
Finding an element in an unsorted list, requires possibly traversing the entire list.



---


---

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

lambda is a unnamed function.
Python allows you to pass functions as arguments. If you have a utility method that is only used in one place, 
you can define it as a lambda instead.
 
An example of passing a lambda is to the sort function.
Lets take the list of tuples (name,score) and , we want to sort it by score descending

    scores=[("sam",80),("alice",20)]

We can do:

    sorted(scores,key= lambda t:-t[1])

---


---

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are a concise way to produce lists
Here is an example to produce a list of numbers from 0 to 9

    [i for i in range(0,10)]
    
Here is the above example, using map

     map(lambda i: i, range(0,10))
     

Lets, say you have a list of number and you are only interested in even numbers

    numbers=[1,2,3,4,5,6]
Below is the code using filter

    filter(lambda i: i%2 ==0, numbers)
    
And here is the code using list comprehensions

    [i for i in numbers if i%2 ==0]

List comprehension and map/filter have the same capabilities

Set comprehension allows you to define a set inline 

    number_set={1,2,3,4}
    

Dictionary comprehension allows you to define a dictionary inline 

    number_dict={"a":1,"b":2}


---


Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.
