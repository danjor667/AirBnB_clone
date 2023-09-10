#!/usr/bin/python3
"""
doc
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    doc
    """
    prompt = "(hbnb) "
    classes = ("BaseModel", "User", "Place", "City",
               "Amenity", "Review", "State")

    def do_quit(self, arg):
        """
        exiting the console
        """
        return True

    def do_EOF(self, arg):
        """
        keyboard interuption
        """
        return True

    def precmd(self, arg):
        """
        doc
        """
        if not arg:
            pass
        else:
            if arg.split()[0] in ("update", "count", "all", "create",
                                  "show", "destroy"):
                return arg
            else:
                myclass = arg.split(".")[0]
                try:
                    mycmd = arg.split(".")[1].strip(")")
                    mycmd = mycmd.strip("(")
                    return " ".join([mycmd, myclass])
                except IndexError:
                    pass
                return myclass
        return arg

    def emptyline(self):
        """
        doc
        """
        pass

    def do_create(self, arg):
        """
        create a new instance of a class
        ex: create Base model
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg.strip() in HBNBCommand.classes:
            obj = eval(arg.strip())()
            storage.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """
        counting the
        the number if instance
        of a particular class
        """
        count = 0
        for k in storage.all().keys():
            if arg == k.split(".")[0]:
                count += 1
        print(count)

    def do_all(self, arg):
        """
        show all objects created if used with no
        parameter
        ex: all
        or
        all BaseModel
        to show all BaseModel objects
        """
        my_list = []
        args = arg.split()
        if len(args) >= 1:
            if args[0] in HBNBCommand.classes:
                key = args[0]
                for k, v in storage.all().items():
                    if k.startswith(key):
                        my_list.append(str(v))
                print(my_list)
            else:
                print("** class doesn't exist **")
        elif len(args) == 0:
            for values in storage.all().values():
                my_list.append(str(values))
            print(my_list)

    def do_show(self, arg):
        """
        show a particular object
        by passing as parameter the class
        and the object id
        ex:
        show BaseModel 78377hd99yhd
        """
        args = arg.split()
        if len(args) >= 2:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print(storage.all().get(key))
                else:
                    print("** no instance found **")
        elif len(args) == 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) == 0:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        deleting an object by passing
        the object's class and id
        ex:
        destroy BaseModel 8uu3uie90u39
        """
        args = arg.split()
        if len(args) >= 2:
            if args[0] in HBNBCommand.classes:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    storage.destroy(key)
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 1:
            if args[0] in HBNBCommand.classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 0:
            print("** class name missing **")

    def do_update(self, arg):
        """
        update the attribute of an object
        passing as parameters the class,
        the id, the attribut and value
        ex:
        update BaseModel 89398838 email "888@.com"
        """
        args = arg.split()
        if len(args) >= 4:
            if args[0] in HBNBCommand.classes:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    setattr(storage.all()[key], args[2],
                            str(args[3].strip('"')))
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 3:
            if args[0] in HBNBCommand.classes:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print("** value missing **")
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 2:
            if args[0] in HBNBCommand.classes:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 1:
            if args[0] in HBNBCommand.classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 0:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
