# Javascript coding convention.

- 2 space indents.
- private methods begin with preceeding underscore.
- all new classes have a documentation block describing their responsibility.
- constants are ALL_UPPER_CASE
- Everything must pass jshint using the checked in config.
- declarations with var always (eg no implicit global objects)
- variables should be camelCasedLikeThis not snake_cased_like_this
- use bower for external dependencies, adding AMD shimming if necessary.
- handlebars templates should be loaded with the `hbs!` require extension, not the `text!` require extension.
- multiple variables are either default-initialized, or separated one per line.

```js
// GOOD
var x = 1;
var y = 2;

var x, y, z;

// BAD
var x = 1, y, z;
var x = 1, y = 2;
```

- Do not throw strings as exceptions.

```js
// GOOD
throw new Error("text here")
// BAD
throw "text here"
```
- Do not use bitwise operators unless doing actual bit manipulation.

```js
// GOOD
Math.floor(1.2)

// BAD
~~1.2  // turns the number into 1
```

- Do not use preceeding `+` to convert string to number.
```js
// GOOD
Number('1.2')

// BAD
+'1.2'
```

- Prefer to ellide else statements for ifs that early return.

```js
// GOOD
if (x) {
  return 1
}
return 2

// BAD
if (x) {
  return 1
} else {
  return 2
}
```
