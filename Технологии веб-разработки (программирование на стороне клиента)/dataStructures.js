/*
2.1. Используя методы строк at, split и toUpperCase, создайте функцию,  которая преобразует строку вида
"background-color" в "backgroundColor",  т.е. удаляет знак "-" и преобразует последующую букву в заглавную.
 */
function convertToCamelCase(str) {
  var words = str.split('-');
  for (var i = 1; i < words.length; i++) {
    words[i] = words[i].charAt(0).toUpperCase() + words[i].slice(1);
  }
  return words.join('');
}

var input = "background-color";
var output = convertToCamelCase(input);
console.log(output); // "backgroundColor"

/*
2.2. Задан массив [9,8,7,6,5,4,3,2,1]. Создайте две копии данного массива разными способами и поменяйте в них
порядок на обратный так же двумя способами. Выведите все три массива.
 */
const originalArray = [9, 8, 7, 6, 5, 4, 3, 2, 1];

const copy1 = [...originalArray];
const reversedCopy1 = copy1.reverse();

const copy2 = originalArray.slice();
const reversedCopy2 = copy2.reverse();

console.log("Original Array:", originalArray);
console.log("Copy 1:", copy1);
console.log("Reversed Copy 1:", reversedCopy1);
console.log("Copy 2:", copy2);
console.log("Reversed Copy 2:", reversedCopy2);

/*
2.3. Используя ассоциативный массив, создайте функцию для перевода заданной строки на необходимый язык.
Переводимые слова и фразы ограничены заданным набором (для примера 4 слова).
 */
const translations = {
  hello: {
    english: "Hello",
    spanish: "Hola",
    french: "Bonjour",
    german: "Hallo"
  },
  goodbye: {
    english: "Goodbye",
    spanish: "Adiós",
    french: "Au revoir",
    german: "Auf Wiedersehen"
  },
};

function translateString(string, language) {
  const translation = translations[string][language];
  return translation ? translation : "Translation not found";
}

const stringToTranslate = "hello";
const languageToTranslate = "spanish";
const translatedString = translateString(stringToTranslate, languageToTranslate);

console.log(`Translation of "${stringToTranslate}" in ${languageToTranslate}: ${translatedString}`);

/*
2.4. Создайте объект с днями недели. Ключами в нем должны служить номера дней от начала недели
(понедельник - первый и т.д.). Выведете текущий день недели.
 */
const daysOfWeek = {
  1: "Monday",
  2: "Tuesday",
  3: "Wednesday",
  4: "Thursday",
  5: "Friday",
  6: "Saturday",
  7: "Sunday"
};

const currentDate = new Date();
const currentDayOfWeek = currentDate.getDay();

console.log("Current day of the week:", daysOfWeek[currentDayOfWeek]);

/*
2.5. Создайте объект "персонал", содержащий должности и имена. Скопируйте его в объект "персонал 2" и поменяйте
в нем имена. Выведите оба объекта, предварительно преобразовав их в строку и используя знаки переноса строки.
 */
const personnel = {
  position1: "John",
  position2: "Jane",
  position3: "Mike"
};

const personnel2 = Object.assign({}, personnel);
personnel2.position1 = "Alice";
personnel2.position2 = "Bob";

console.log("Personnel 1:\n", JSON.stringify(personnel, null, 2));
console.log("Personnel 2:\n", JSON.stringify(personnel2, null, 2));

/*
2.6. Есть переменная, в которую через запятую перечислены сокращения дней недели. Преобразовав данную переменную
в массив и используя перебор, добавьте к заданию №3 новое свойство объекта. Создайте метод вывода на экран
сокращенного текущего дня недели.
 */
const daysOfWeekAbbreviations = "Mon,Tue,Wed,Thu,Fri,Sat,Sun";

const daysOfWeek = {};

function addAbbreviatedWeekdays(obj, abbreviations) {
  const weekdays = abbreviations.split(",");
  obj.abbreviatedWeekdays = weekdays;
}

addAbbreviatedWeekdays(daysOfWeek, daysOfWeekAbbreviations);

console.log("Updated daysOfWeek object:", daysOfWeek);

daysOfWeek.displayAbbreviatedCurrentDay = function() {
  const currentDate = new Date();
  const currentDayOfWeek = currentDate.getDay();
  const abbreviatedCurrentDay = this.abbreviatedWeekdays[currentDayOfWeek - 1];
  console.log("Abbreviated current day of the week:", abbreviatedCurrentDay);
};

daysOfWeek.displayAbbreviatedCurrentDay();

/*
2.7.  Создайте объект "предметы", со свойством, в котором через запятую перечислены предметы, преподаваемые в
университете/школе(перечислите 2-6). Напишите к нему функцию, которая будет добавлять предмет, если его еще там нет.
Используйте для этого преобразование в массив и свойства массивов split, join, push.

Дополнение*: Удалите предмет, если он уже там есть с помощью свойства splice.
 */
const subjects = {
  list: "Math,Physics,Chemistry,Biology"
};

function addSubject(subject, obj) {
  const subjectList = obj.list.split(",");
  if (!subjectList.includes(subject)) {
    subjectList.push(subject);
    obj.list = subjectList.join(",");
  }
}

addSubject("Computer Science", subjects);
addSubject("Math", subjects);

console.log("Updated subjects object:", subjects);

subjects.removeSubject = function(subject) {
  const subjectList = this.list.split(",");
  const index = subjectList.indexOf(subject);
  if (index !== -1) {
    subjectList.splice(index, 1);
    this.list = subjectList.join(",");
  }
};

subjects.removeSubject("Physics");
console.log("Updated subjects object after removing Physics:", subjects);