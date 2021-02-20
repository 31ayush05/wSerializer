# wSerializer v0.6
A python library capable of serializing data and storing them as text file and then also retrieving it from the text file. The code is also capable of encrypting the text file so that it cannot be edited externally thus protecting the data.
The current version is not capable of encryptng the file.

v0.6 updates
variable values can be updated and new variables can be added just like dicitionaries `<dataBlock variable name>[key] = value`.
Deserialize() function is discontinued as its useless.
dataFiles now get compressed (was required since the data tags took up a huge amount of space).
now `in` function can be used to see if a variable exisst or not.

Authur - Ayush Yadav
GITHUB - https://github.com/31ayush05
REPO - https://github.com/31ayush05/wSerializer
Documentation - https://github.com/31ayush05/wSerializer/wiki/Documentation

OFFLINE DOCUMENTATION

# Installation
Currently the module cannot be installed using `PIP`. But it can easily be installed the other way.
### STEPS
1. Download the latest version of repository as a ZIP file from https://github.com/31ayush05/wSerializer/releases/tag/v0.5
2. Extract the ZIP file and copy the code file `Serializer\wSerializer.py`.
3. Locate the python installation folder on your PC which can be done by RIGHT CLICKING on the PYTHON IDLE > Open file location.
4. Paste the file in the `<Python installation folder>\Lib\`
5. Now the module is ready to be imported in any of your python project.

# How To Use

> in the entire documentation by **RAM** I mean a local variable present within the `dataBlock class`

## Importing
use the following statement to import the module

`import wSerializer`

## Concept behind the module
The module consists of a class `dataBlock` the `dataBlock` is responsible for storing the variable names with their specific values. The same class `dataBlock` will also retrieve the data.

***

## Coding
### Defining a `dataBlock` variable
Defining a `dataBlock` is very simple. The syntax for the same is as follows.

`<variable name> = wSerializer.dataBlock(filePath, autoSync, showCompression)`

* `filePath`(str) - It is the path of the text file to which you want to serialize(store) your data or the file from which you want to Deserialize(retrieve) the data.
* `autoSync`(bool) - _**Default = True**_
  * If set `True` - the text file is kept up-to-date by updating the file as soon as you add more variables to `dataBlock`.
    * This can be used when the data file needs to remain up-to-date
  * If set `False` - the text file is not kept up-to-date instead you have to call the function `Serialize()` every time you want to update the text file.
    * This can come handy when you want to update the file after you have collected all necessary data.
* `showCompression`(bool) - _**Default = False**_
  * If set `True` displays the percentage by which the data file was compressed.
  * If set `False` does not display the percentage.

#### NOTE
> The `dataBlock` keeps all your variables stored in RAM as long as the code is running
> Therefore, it might happen that you **TURN OFF** the _Auto Update_ feature and **FORGET TO UPDATE THE DATA FILE**. Thus, the data file is not up-to-date but you can still access those variables. 

> **JUST DONT FORGET TO UPDATE DATA FILE IF YOU HAVE TURNED OFF AUTO UPDATE**

##### **EXAMPLES**
```
import wSerializer as SL

dB = SL.dataBlock('E://testing.txt')
```
Here we have created a `dataBlock` named `dB` with the text file path set to `'E://testing.txt'` and we have enabled `autoSync`.
Thus the data will be synced with the text file.

***

### `Add(name, value)`
Adds a new variable to the `dataBlock`

SYNTAX 

`<dataBlock variable name>.Add(name, value)`

* name - it is the name of the variable
  * It can only be of the types - 
    - str
    - int 
    - float
    - bool
    - complex
* value - it is the value of the variable
  * It can only be of the types
    - str
    - int 
    - float
    - bool
    - complex
    - list
    - tuple
    - set
    - dict

#### NOTE
> The `name` and the `value` cannot be any of the following
> '|↑|int|↑|'
> '|↓|int|↓|'
> '|↑int↑|'
> '|↑|str|↑|'
> '|↓|str|↓|'
> '|↑str↑|'
> '|↑|float|↑|'
> '|↓|float|↓|'
> '|↑float↑|'
> '|↑|bool|↑|'
> '|↓|bool|↓|'
> '|↑bool↑|'
> '|↑|complex|↑|'
> '|↓|complex|↓|'
> '|↑complex↑|'
> '|↑|dict|↑|'
> '|↓|dict|↓|'
> '|↑|dictInList|↑|'
> '|↓|dictInList|↓|'
> '|↑|list|↑|'
> '|↓|list|↓|'
> '|↑l↑|'
> '|↓l↓|'
> '|↑|tuple|↑|'
> '|↓|tuple|↓|'
> '|↑t↑|'
> '|↓t↓|'
> '|↑|set|↑|'
> '|↓|set|↓|'
> '|↑s↑|'
> '|↓s↓|'

##### **EXAMPLES**
```
import wSerializer as SL

dB = SL.dataBlock('E://testing.txt')

dB.Add('name' , 'CHINTU')
dB.Add('age' , 8)
dB.Add('Hobby' , 'CODING')
```

Here the data `{'name' : 'CHINTU' , 'age' : 8 , 'Hobby' : 'Coding'}` is added and is synced with the text file. and can be accessed even if we rerun the program.

```
import wSerializer as SL

dB = SL.dataBlock('E://testing.txt', False)

dB.Add('name' , 'CHINTU')
dB.Add('age' , 8)
dB.Add('Hobby' , 'CODING')
```

Now the data `{'name' : 'CHINTU' , 'age' : 8 , 'Hobby' : 'Coding'}` isn't synced with the file and after the execution of the above statements the data is stored in RAM but not in the text file. So, if the program is closed and started again the data is not present in the file and thus cannot be accessed.

***

### `Remove(name)`
Removes a pre-defined variable in the `datablock`

SYNTAX

`<dataBlock variable name>.Remove(name)`

name - It is the name of the variable which you want to remove from the `dataBlock`

#### NOTE
> IF the `name` does not exist in the `dataBlock`. The following message is printed on the screen.

> "Defined variable does not exist in the dataBlock"

##### **EXAMPLES**
```
import wSerializer as SL

dB = SL.dataBlock('E://testing.txt')

dB.Add('name' , 'CHINTU')
dB.Add('age' , 8)
dB.Add('Hobby' , 'CODING')
dB.Remove('Hobby')
```

now `'Hobby'` will be removed.

`data = {'name' : 'CHINTU' , 'age' : 8}`

***

### Accessing a variable
SYNTAX

`<dataBlock variable name>[name]`

name - it is the name of the variable you want to access.

##### **EXAMPLES**
```
import wSerializer as SL

dB = SL.dataBlock('E://testing.txt')

dB.Add('name' , 'CHINTU')
dB.Add('age' , 8)
dB.Add('Hobby' , 'CODING')

print(dB['age'])
```

The last statement will print `8`.

If we close the above code and run the following code instead

```
import wSerializer as SL

dB = SL.dataBlock('E://testing.txt')

print(dB['name'])
print(dB['age'])
print(dB['Hobby'])
```

The output will be - 

```
CHINTU
8
CODING
```

This happened because we did not delete the text file and accessed it using `dB = SL.dataBlock('E://testing.txt', True)` statement.

***

### `in`

This statement can be used to see weather a particular variable exists in the code or not.

##### **EXAMPLES**
```
import wSerializer as SL

dB = SL.dataBlock('E://testing.txt')

dB.Add('name' , 'CHINTU')
dB.Add('age' , 8)
dB.Add('Hobby' , 'CODING')

print('name' in dB)
print('class' in dB)
```
The output will be
```
True
False
```
because `name` exists while `class` doesn't

***

### Updating a value

`<dataBlock variable name>[<variable name>] = <value>`

if <variable name> exists then its value is updated otherwise new variable with the given value is added.

##### EXAMPLES
```
import wSerializer as SL

dB = SL.dataBlock('E://testing.txt')

dB.Add('name' , 'CHINTU')
dB.Add('age' , 8)

print(dB['age'])
```
the above code will create a dataFile named testing.txt and will store `{'name' : 'CHINTU', 'age' : 8}` in the file.

Now if we run the following code
```
import wSerializer as SL

dB = SL.dataBlock('E://testing.txt')

dB['age'] = 9
dB['Hobby'] = 'CODING'

print(dB['age'])
```
Since variable name `'age'` already exists its value will be updated to `9` while a new variable named `'Hobby'` will be added with the value `'CODING'`.
Therefore the data stored becomes `{'name' : 'CHINTU', 'age' : 9, 'Hobby' : 'CODING'}`

> Thus this method can be used to Add new values to the dataBase.

***

### Printing the entire data base

just use the code  `print(<dataBlock variable>)` and the entire dataBase will be printed.

##### **EXAMPLES**
```
import wSerializer as SL

dB = SL.dataBlock('E://testing.txt')

dB.Add('name' , 'CHINTU')
dB.Add('age' , 8)
dB.Add('Hobby' , 'CODING')

print(dB)
```

output will be

```
name : str - str
     CHINTU
age : str - int
     8
Hobby : str - str
     CODING
```
Here
Statement 1 
```
name : str - str
     CHINTU
```
states that `VARIABLE NAME = 'name'`
`str - str` states that variable name is of type `str` and the value is also a `str`
same goes for all other STATEMENTS  

***

### `Reset()`

SNTAX

`<dataBlock variable name>.Reset()`

Cleans the stated text file. If the file does not exist creates a new blank file.

```
import wSerializer as SL

dB = SL.dataBlock('E://testing.txt')

dB.Add('name' , 'CHINTU')
dB.Add('age' , 8)
dB.Add('Hobby' , 'CODING')
```

Executing the above code will result in data being saved to the text file

```
import wSerializer as SL

dB = SL.dataBlock('E://testing.txt')

dB.Reset()
```

Now the data file is cleaned

***

### `Serialize()`

Writes the data in the text file. 

SYNTAX

`<dataBlock variable name>.Serialize()`

This function is called automatically when `autoSync` set to `True`

```
import wSerializer as SL

dB = SL.dataBlock('E://testing.txt', False)

dB.Add('name' , 'CHINTU')
dB.Add('age' , 8)
dB.Add('Hobby' , 'CODING')
dB.Serialize()
```

Since `autoSync` was **turned OFF** we had to `Serialize()` manually.
