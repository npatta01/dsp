# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

list environments and search for value of an env

    env | grep TESTING

search in a file

     grep new *.txt
     
edit my path

    nano ~/.bashrc
---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

ls : list files

-l: use a long listing format
-a: show hidden files too (starting with .)
-h: display sizes in human readable form

-lh: display in long listing and in readable form

All three options ls-lah are probably helpful together

---


---

What does `xargs` do? Give an example of how to use it.

Answer based on [here](http://www.cyberciti.biz/faq/linux-unix-bsd-xargs-construct-argument-lists-utility/) 
and [here](https://en.wikipedia.org/wiki/Xargs)

    xargs is a command that can be used be used to construct argument list for other commands.
    Some command might fail if the argument list is too long

    An example
    find all .bak files in the current directory and remove them

    ls *.bak | xargs rm

---
