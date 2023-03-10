#!/usr/bin/python3


from os import systems
from models.engine.file_storage import FileStorage
import unittest
from io import StringIO
from unittest.ock import patch
from console import HBNBCommand
from models import storage

import os


class ConsolePromtingTest(unittest.TestCase):

    def testPrompt(self):
        """
            Prompt command
        """
        self.assertEqual(HBNBCommand().prompt,
                         "(hbnb) ")

    def testEmptyLine(self):
        """
            Empty line
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("")
            self.assertEqual(output.getvalue().strip(), "")


class ConsoleHelpTest(unittest.TestCase):
    def testHelpCreate(self):
        """
            create() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help create")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Creates a new instance of BaseModel, \
saves it (to the JSON file) and prints the id.\n\n")

    def testHelpAll(self):
        """
            all() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help all")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Prints all string representation of \
all instances based or not on the class name.\n\n")

    def testHelpDestroy(self):
        """
            destroy() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help destroy")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Deletes an instance based on the \
class name and id (save the change into the JSON file).\n\n")

    def testHelpUpdate(self):
        """
            update() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help update")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Updates an instance based on the \
class name and id by adding or updating attribute (save the \
change into the JSON file).\n\n")

    def testHelpShow(self):
        """
            show() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help show")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Prints the string representation of \
an instance based on the class name and id.\n\n")

    def testHelpQuit(self):
        """
            quit() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help quit")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Quit command to exit the program\n\n")

    def testHelpEOF(self):
        """
            EOF command have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help EOF")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(),
                             "EOF command to exit the program\n\n")

    def testHelpCount(self):
        """
            count() method have help documented
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help count")
            self.assertGreater(len(output.getvalue()), 0)
            self.assertEqual(output.getvalue(), "Update your command interpreter \
(console.py) to retrieve the number of instances of a class.\
\n\n")

class ConsoleExitTest(unittest.TestCase):

    def testDoQuit(self):
        """
            Quit
        """
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("quit")

    def testDoEOF(self):
        """
            EOF
        """
        with self.assertRaises(SystemExit):
            HBNBCommand().onecmd("EOF")

class ConsoleAllTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

def testAllInvalidClass(self):
        """
            all invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("toto.all()")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    @colorize(color=RED)
    def testAllMissingClass(self):
        """
            all() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(".all()")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    def testAllInstanceSpaceNotation(self):
        """
            all instance command
        """
        self.__allInstanceSpaceNotation("Amenity", "User")
        self.__allInstanceSpaceNotation("BaseModel", "User")
        self.__allInstanceSpaceNotation("City", "User")
        self.__allInstanceSpaceNotation("Place", "User")
        self.__allInstanceSpaceNotation("Review", "User")
        self.__allInstanceSpaceNotation("State", "User")
        self.__allInstanceSpaceNotation("User", "BaseModel")

    def testAllInstanceDotNotation(self):
        """
            all() instance command
        """
        self.__allInstanceDotNotation("Amenity", "User")
        self.__allInstanceDotNotation("BaseModel", "User")
        self.__allInstanceDotNotation("City", "User")
        self.__allInstanceDotNotation("Place", "User")
        self.__allInstanceDotNotation("Review", "User")
        self.__allInstanceDotNotation("State", "User")
        self.__allInstanceDotNotation("User", "BaseModel")

    def __allInstanceSpaceNotation(self, prmClassName, prmOtherClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
        with patch("sys.stdout", new=StringIO()) as output:
            command = "all {}".format(prmClassName)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertIn(prmClassName, output.getvalue().strip())
            self.assertNotIn(prmOtherClassName, output.getvalue().strip())

    def __allInstanceDotNotation(self, prmClassName, prmOtherClassName):
        with patch("sys.stdout", new=StringIO()) as output:
           self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
        with patch("sys.stdout", new=StringIO()) as output:
            command = "{}.all()".format(prmClassName)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertIn(prmClassName, output.getvalue().strip())
            self.assertNotIn(prmOtherClassName, output.getvalue().strip())

class ConsoleCountTest(unittest.TestCase):
    __classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
    ]

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def testCountMissingClass(self):
        """
            count() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("count")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    def testCountInvalidClass(self):
        """
            count() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("count toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def testCountInstanceSpaceNotation(self):
        """
            count instance command
        """
        self.__testCountObject("Amenity")

    def testCountInstanceDotNotation(self):
         """
            count() instance command.
        """
        for className in self.__classes:
            self.__testCountDotNotation(className)

    def __testCountSpaceNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "count {}".format(prmClassName)))
        count = int(output.getvalue())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
        id = output.getvalue()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "count {}".format(prmClassName)))
            self.assertEqual(output.getvalue().strip(), str(count + 1))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

    def __testCountDotNotation(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.count()".format(prmClassName)))
        count = int(output.getvalue())
            
            with patch("sys.stdout", new=StringIO()) as output:
                 self.assertFalse(HBNBCommand().onecmd(
                "create {}".format(prmClassName)))
        id = output.getvalue()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.count()".format(prmClassName)))
            self.assertEqual(output.getvalue().strip(), str(count + 1))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                "{}.destroy({})".format(prmClassName, id)))

class ConsoleCreateTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass


    def testCreateMissingClass(self):
        """
            create() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual(output.getvalue(), "** class name missing **\n")
            
    def testInvalidClass(self):
        """
            create() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def testCreateAmenity(self):
        """
            create() Amenity
        """
        self.__testCreateObject("Amenity")

    def testCreateBaseModel(self):
        """
            create() BaseModel
        """
        self.__testCreateObject("BaseModel")

    def testCreateCity(self):
        """
            create() City
        """
        self.__testCreateObject("City")

    def testCreatePlace(self):
        """
            create() Place
        """
        self.__testCreateObject("Place")

    def testCreateReview(self):
        """
            create() Review
        """
        self.__testCreateObject("Review")

    def testCreateState(self):
        """
            create() State
        """
        self.__testCreateObject("State")

    def testCreateUser(self):
        """
            create() User
        """
        self.__testCreateObject("User")

    def __testCreateObject(self, prmClassName):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create {}".format(prmClassName)))
            testKey = "{}.{}".format(prmClassName, output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

class ConsoleDestroyTest(unittest.TestCase):

    classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    @colorize(color=RED)
    def testDestroyMissingClass(self):
        """
            destroy() missing class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(output.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(".destroy()")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    @colorize(color=RED)
    def testDestroyInvalidClass(self):
        """
            destroy() invalid class
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy toto")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("toto.destroy()")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def testDestroyMissingIdSpaceNotation(self):
        """
            destroy missing id command
        """
        for className in self.__classes:
            self.__missingIdSpaceNotation(className)

    def testDestroyMissingIdDotNotation(self):
        """
            destroy() missing id command
        """
        for className in self.__classes:
            self.__missingIdDotNotation(className)

    def testDestroyNoInstanceFoundSpaceNotation(self):
        """
            destroy no instance command
        """
        for className in self.__classes:
            self.__noInstanceFoundSpaceNotation(className)

    def testDestroyNoInstanceFoundDotNotation(self):
        """
            destroy() no instance command
        """
         for className in self.__classes:
            self.__noInstanceFoundDotNotation(className)

    def testDestroyInstanceSpaceNotation(self):
        """
            destroy instance command
        """
         for className in self.__classes:
            self.__destroyInstanceSpaceNotation(className)

    def testDestroyInstanceDotNotation(self):
        """
            destroy() instance command
        """
         for className in self.__classes:
            self.__destroyInstanceDotNotation(className)
        
class ConsoleTest(unittest.TestCase):
    def testDoCreate(self):
        pass

    def testDoAll(self):
        pass

    def testDoDestroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
        pass	            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 2")
            self.assertEqual(f.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        id = self.__getUuidFromString(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User {}".format(id))
            self.assertEqual(f.getvalue(), "** attribute name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User {} first_name".format(id))
            self.assertEqual(f.getvalue(), "** value missing **\n")
        obj = self.__getCurrentObject("User", id)
        self.assertEqual(obj.first_name, '')
        HBNBCommand().onecmd("update User {} first_name 'John'".format(id))
        obj = self.__getCurrentObject("User", id)
        self.assertEqual(obj.first_name, 'John')
        HBNBCommand().onecmd("update User {} age 89".format(id))
        self.assertEqual(obj.first_name, 'John')
        self.assertEqual(obj.age, 89)

     def testDoUpdate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update toto")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def testDoShow(self):
        pass
