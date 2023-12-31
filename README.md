# Handy
## Why ?
In javascript when you work with arrays, you can do some chaining operation in a functional programming style like : 
```javascript
jsList = [1, 2, 3, 4]
console.log(jsList.map(el => el * 2))
>>> [ 2, 4, 6, 8 ]
jsList = [1, 2, 3, 4]
console.log(jsList.filter(el => el % 2 == 0).map(el => el + 1))
[ 3, 5 ]
```
Python offers functools with `map` and `filter` but they are not as handy 
as in javascript when we want to chain them in FP style.

This is why i'm proposing this package that offers 2 objects, `SmartList`
that act as a simple wrapper on standard list and offers methods like (map,sort, filter_by_redicates, filter_by_val_attributes etc...) and `ObjectDict` that 
act as a wrapper on a normal dict, and allow access to it's
values directly as if they were attributes of the object (works also with nested dict).

So `SmartList` used in combination with `ObjectDict` offers you the same
experience as you would have in javascript, in some scenarios i found this
pattern really handy to extract the data i want from 3rd party apis when they
were not granular enough
.
## Usage
```python
# Condider we have the following list of dict 
ldict = [{'name': 'Kenneth Thomas',
  'job': 'Broadcast presenter',
  'company': 'Williams-Miller'},
 {'name': 'Edward Hamilton',
  'job': 'Quarry manager',
  'company': 'Anderson-Kline'},
 {'name': 'Brandon Weeks',
  'job': 'Theme park manager',
  'company': 'Williams, Garcia and Allen'},
 {'name': 'Kim Little',
  'job': 'Insurance risk surveyor',
  'company': 'Frank-Hutchinson'},
 {'name': 'David Gutierrez',
  'job': 'Community pharmacist',
  'company': 'Allen, Herman and Ellis'},
 {'name': 'Matthew Cook',
  'job': 'Chief Operating Officer',
  'company': 'Hansen-Young'},
 {'name': 'Mark Watson',
  'job': 'Doctor, general practice',
  'company': 'Vargas PLC'},
 {'name': 'Jessica Ellis',
  'job': 'Tourist information centre manager',
  'company': 'Williams-Reeves'},
 {'name': 'Jessica Duncan',
  'job': 'Administrator, Civil Service',
  'company': 'Hobbs Group'},
 {'name': 'Diana Butler',
  'job': 'Scientist, research (maths)',
  'company': 'Olsen, Maddox and Smith'}]

# Consider i want extract just people that work as managers, here is how i do 
from handy import SmartList, ObjectDict
managers = SmartList(ldict).map(lambda el : ObjectDict(el)).filter_by_predicates(lambda el : "manager" in  el.job.lower())

>>> [{'name': 'Edward Hamilton',
  'job': 'Quarry manager',
  'company': 'Anderson-Kline'},
 {'name': 'Brandon Weeks',
  'job': 'Theme park manager',
  'company': 'Williams, Garcia and Allen'},
 {'name': 'Jessica Ellis',
  'job': 'Tourist information centre manager',
  'company': 'Williams-Reeves'}]
# There are more things you can do with the methods of smart list, like aggregation by predicates, or check attribute equality or pattern matching
# len -> gives you lenght of your list 
# map -> map your list to a new list
# first -> give you first element of list (index error if doesnt exist)
# last -> give you last element of list (index error if doesnt exist)
# last_or_none  -> give you last element of list (None if doesn't exist)
# first_or_none  -> give you first element of list (None if doesn't exist)
# one_or_none -> one element or None otherwise
# sort -> sort your list to a new list 
# filter_by_predicates -> filter by predicates (functions that return true or false)
# filter_by_attribute_values -> filter by keyword attribute values()
# filter_by_matched_attributes -> filter by keyword patterns values()
# group_by_labeled_predicates -> group by [(label, predicate)], you obtain a SmartList of tuples [(label, filtered_smart_list)]

```
