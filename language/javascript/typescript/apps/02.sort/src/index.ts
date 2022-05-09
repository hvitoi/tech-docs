import { NumbersCollection } from './NumbersCollection';
import { CharactersCollection } from './CharactersCollection';
import { LinkedList } from './LinkedList';

// NUMBERS
const numbersCollection = new NumbersCollection([2, 1, 0, -1, -2]);
numbersCollection.sort();
console.log(numbersCollection.data);

// CHARACTERS
const charactersCollection = new CharactersCollection('CbcBaa');
charactersCollection.sort();
console.log(charactersCollection.data);

// LINKED LIST
const linkedList = new LinkedList();
linkedList.add(2);
linkedList.add(1);
linkedList.add(0);
linkedList.add(-1);
linkedList.add(-2);

linkedList.sort();
linkedList.print();
