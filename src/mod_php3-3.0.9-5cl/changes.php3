<!-- X-URL: http://www.php.net/changes.php3 -->
<BASE HREF="http://www.php.net/changes.php3">

<html><head><title>PHP3 Changes</title></head>
<body bgcolor="#ffffff" text="#032F5B" link="#537492" vlink="#000000">
<FONT FACE="Verdana, Arial, Helvetica">
<PRE><h1>Noticeable Changes between <i>PHP</i> 2.0 and <i>PHP</i> 3.0</h1>
<i>(written by Zeev Suraski)</i>

First, please note that the core of <i>PHP</i> 3.0 is a *complete* rewrite
from scratch.  Things that may have been undocumented features of <i>PHP</i> 2.0
(due to low-level implementation) are likely not to work in this release.

In addition, several changes were made to the language that are downwards
incompatible.


<h2>Incompatabilities</h2>

<font size=+1><b><i>[1] The close-<i>PHP</i> tag has changed from > to ?>
</i></b></font>
This means that instead of writing:

	&lt;?echo $title;>

You should write:

	&lt;?echo $title;?>

<i>PHP</i>3 also includes support for a longer-form start tag that is
XML-compliant. To wit:

	&lt;?php echo $title;?>

The ability to use the short start tag ('&lt;?') can be turned on and
off using the short_tags() function. Whether it is enabled or not by
default is a compile-time option (normally set to enabled by default).

<font size=+1><b><i>[2] Semicolons in if/elseif/else must be replaced with colons.
</i></b></font>
For example, the equivalent of:

	if (expr);
	  statements
	  ...
	elseif (expr);
	  statements
	  ...
	else;
	  statements
	endif;

in <i>PHP</i> 3.0 would be:

	if (expr):
	  statements
	  ...
	elseif (expr):
	  statements
	  ...
	else:
	  statements
	endif;

Note that the endif is followed by a semicolon and not a colon even in
<i>PHP</i> 3.0, which marks the end of the entire IF sentence.

Also note that the implementation of the colon-mode and curly-braces
mode in <i>PHP</i> 3.0 is identical, one isn't buggier than the other.

<font size=+1><b><i>[3] Semicolons in while loops must also be replaced with colons.
</i></b></font>
For example, the equivalent of:

	while (expr);
	  statements
	  ...
	endwhile;

in <i>PHP</i> 3.0 would be:

	while (expr):
	  statements
	  ...
	endwhile;

Note that the endwhile is followed by a semicolon and not a colon even
in <i>PHP</i> 3.0, which marks the end of the WHILE sentence.  As with the IF
statement, the implementation of the colon-mode and curly-braces mode
in <i>PHP</i> 3.0 is identical, one isn't buggier than the other.

Also note that failing to change the semicolon to a colon can result in
scripts that get stuck in the while loop because the loop-condition never
changes.

<font size=+1><b><i>[4] $foo[0] is no longer identical to $foo.
</i></b></font>
In <i>PHP</i> 2.0, a side-effect of the implementation caused $foo[0] to be
identical to $foo.  This is not the case in <i>PHP</i> 3.0.

<font size=+1><b><i>[5] Expressions determine their types differently.
</i></b></font>
The way expressions are evaluated has changed radically in <i>PHP</i> 3.0.
Expressions are no longer given the type of the left argument, but are
assigned types taking both types into account, and regardless of which
is on the left side and which is on the right side.  On simple scripts
that should probably not effect you, but if you've relied on this fact
(even without realizing you do) it may change the way your scripts work.
Consider the next example:

	$a[0]=5;
	$a[1]=7;

	$key = key($a);
	while ("" != $key) {
		echo "$keyn";
		next($a);
	}


In <i>PHP</i> 2.0, this would display both of $a's indices.  In <i>PHP</i> 3.0, it
wouldn't display anything.  The reason is that in <i>PHP</i> 2.0, because the
left argument's type was string, a string comparison was made, and indeed
"" does not equal "0", and the loop went through.  In <i>PHP</i> 3.0, when a
string is compared with an integer, an integer comparison is made (the
string is converted to an integer).  This results in comparing atoi("")
which is 0, and $key which is also 0, and since 0==0, the loop doesn't
go through even once.  The fix for this is simple, by replacing the
while statement with:

	while ("" != stringval($key)) {

This would first convert the integer 0 to a string "0", and then
compare "" and "0", which are not equal, and the loop would go through
as expected.  As mentioned later, casting operators are supported in
<i>PHP</i> 3.0 for a quicker and more readable way of changing variables'
types. For example, you could use:

	while ("" != (string)$key) {

<font size=+1><b><i>[6] The plus (+) and minus (-) operators are no longer overloaded for
</i></b></font>    string operations.

In <i>PHP</i>2, you could add two strings together to get their concatenation,
and subtract them to remove all occurences of one from the other.

In <i>PHP</i>3, you should use the string concatenation operator (.) to
concatenate strings, and the ereg_replace function to replace or
remove substrings from a string. For example:

	$a = 123;
	$string = "This is as easy as " . $a;
	$string = ereg_replace("This is as easy as ", "", $string);

<font size=+1><b><i>[7] The structure of error messages has changed.
</i></b></font>
Although the error messages are usually more accurate, you won't be shown
the actual line of text and actual place in which the error occured.
You'll be supplied with the line number in which the error has occured,
though.

<font size=+1><b><i>[8] The format string argument to echo is no longer supported.
</i></b></font>
Use printf(format,arg1,arg2,arg3,...) instead (unlimited arguments).

<font size=+1><b><i>[9] The use of read-mode $array[] is no longer supported.
</i></b></font>
That is, you cannot traverse an array by having a loop that does $data =
$array[].  Use current() and next() instead.  Also, $array1[] = $array2
does not append the values of $array2 to $array1, but appends $array2
as the last entry of $array1 (see the multidimensional array support).

<font size=+1><b><i>[10] Apache versions older than 1.2 are no longer supported.
</i></b></font>
The Apache module requires Apache 1.2 or later (1.3-beta is supported).

<font size=+1><b><i>[11] Page logging and access restrictions are no longer supported
</i></b></font>
The development team believes that this functionality does not belong
in the core of <i>PHP</i>, and thus, it's been dropped in version 3.0.
Page logging can be implemented using auto-appended or prepended
scripts without internal support in the core (a DBM logging script
is available).

Access restrictions are available internally in just about any
modern web server.

<font size=+1><b><i>[12] Indirect references inside quoted strings
</i></b></font>
<i>PHP</i>2-style indirect reference inside quoted strings is no longer
supported.  That is, if $foo="bar", and $bar="abc", in <i>PHP</i>2, "$$foo"
would print out "abc".  In <i>PHP</i>3, this would print "$bar" (the contents
of $foo is replaced with "bar").  To use indirect reference in <i>PHP</i>3
inside quoted strings, you should use the new notation: "${$foo}".
The standard $$foo notation will work outside of the quoted string.


<font size=+1><b><i>[13]    Some functions have changed names, are missing, or have been deprecated
</i></b></font>        by other functions

As a whole new rewrite, written by many more people and supporting many
more APIs than it's predecessor, there's a good chance some of the functions
you're used to from <i>PHP</i>/<i>FI</i> 2 aren't available in release 3, or have changed
names.  Many functions that do exist behave a bit differently, mainly
because they return different values for errors (false) but also for other
reasons.  We can't list all of these functions here, simply because drawing
a full comparison between the function sets of the two versions is way too
much work.  If a converted <i>PHP</i>/<i>FI</i> 2 script doesn't work for you, nothing
can replace the good old human eye going over the code, doublechecking
with the online manual that each function still does what you expected it
to do.

<font size=+1><b><i>[14] Other incompatibilities.
</i></b></font>
It's not too unlikely that other documented behavior of <i>PHP</i>2 has changed
in this release.  If you think you've found an example, please mail
us at php-dev@php.iquest.net.  Even if you've found an undocumented
feature of <i>PHP</i>2 that stopped working in <i>PHP</i>3, we'd like to know about it
(although it's more than likely that it will not be supported).

And now, the fun part.

<h2>New Language Features</h2>

<font size=+1><b><i>[1] Expressions
</i></b></font>
<i>PHP</i> 3.0 includes a rich implementation of expressions, much more advanced
than this of 2.0.  Just about any complex C-like or perl-like expression
would work.  Support was added for assignment operators (+=, -=, *= etc),
pre and post increment/decerement (e.g. $i++, ++$i) and the questionmark
operator ( (expr?expr:expr) ).  Every assignment is now an expression
with a value, which means stuff like $a = $b = $c = $d = 0;  would work.
It is difficult to describe the power of expressions within a few lines
of text, but if you're familiar with them, you probably get the picture.

<font size=+1><b><i>[2] for loops are now supported.
</i></b></font>
for loops were fairly difficult to implement (in fact, we didn't find
any parallel interpreter that supports for loops anywhere (no, perl is
not an interpreter)).  The bottom line is that for loops work, and are
around 5% slower than comparable while loops (that may vary), but often
they're much nicer.

The syntax is identical to the one of C:

	for (expr; expr; expr) statement;

or

	for (expr; expr; expr) { statements ... }

The first expression is executed the first time the loop is encountered,
the loop is run as long as the second expression is evaluated as TRUE,
and after each iteration, the 3rd expression is evaluated.


Colon-mode FOR loops are also supported:

    for (expr; expr; expr):
        statements
        ...
    endfor;

<font size=+1><b><i>[3] do..while(expr) loops are now supported.
</i></b></font>
Like with its C parallel, the statements inside a do..while loop are
run once the first time the loop is encountered, and then as long as
the expression evaluates as true.

For example:

	do {
		statements;
	} while ($i++ < $max);

<font size=+1><b><i>[4] break and continue statements are now supported inside loops.
</i></b></font>
You can break out of loops, or continue to the next iteration of the
loop using these statements.  A special feature of <i>PHP</i> is the ability
to specify an expression argument to break or continue, which specifies
how many loops you want to break out from or continue to.  For example:

	for ($i=0; $i<10; $i++) {
		for ($j=0; $j<10; $j++) {
			if ($j>5)
				break;
			if ($i>5)
				break 2;
		}
	}

The first break statement would end the inner loop every time $j is
greater than 5.  The second break statement would end both the inner
and outer loop when $i is greater than 5.

Note:  For this matter, switch statements are considered as loops.  So
if you write "break 2;" inside a switch statement, you would be asking
to break out of the switch, and the innermost loop in which is nested.

<font size=+1><b><i>[5] Support for C-style declaration of functions.
</i></b></font>
Here's a pretty useless function which makes a good example:

	function concat($str1,$str2)
	{
		return $str1.$str2;
	}

* Old-style function declerations should be changed from function to old_function

<font size=+1><b><i>[6] OOP support
</i></b></font>
Classes and inheritance are supported to a limited extent in <i>PHP</i> 3.0.
Here's how to declare a simple class:

	class simple_class {
		var $property1,$property2;
		var $property3=5;

		function display() {
			printf("p1=%d, p2=%d, p3=%dn",
				$this->property1,
				$this->property2,
				$this->property3);
		}
		function init($p1,$p2) {
			$this->property1 = $p1;
			$this->property2 = $p2;
		}
	};

Here's how to create an object of that class:

	$obj = new simple_class;

At this point, $obj is an object with 2 uninitialized variables, 1
initialized variable, and 2 member functions.  No protection is made on
the internals of the object, and using its properties is simple:

	$obj->property1 = 7;

would assign 7 to $property1 inside $obj.  Calling member functions is
also simple:

	$obj->display()

would run the display() member function of $obj.  Note that the
implementation of display() uses the special variable $this, which is
replaced with the object the function is called on.

Inheritance is pretty simple too:

	class complex_class extends simple_class {
		var $property4="test";

		function display() {
			printf("p1=%d, p2=%d, p3=%d, p4=%dn",
				$this->property1,
				$this->property2,
				$this->property3,
				$this->property4);
		}
	}

Basically, the class complex_class inherits everything from its parent,
simple_class, except properties or member functions which override the
ones in the parent.  In this example, since we supply an alternative
display() function, it would be used with complex_class objects instead
of the display() function that was declared in simple_class.  On the other
hand, since we don't supply an alternative init() function, complex_class
objects would have the same init() function as simple_class objects do.

As with expressions, it's impossible to teach OOP in a few lines, and
personally I'm unclear as to how useful this would be in day to day
scripting.  If you like this, play with this until you figure it out :)

Note:  A limitation of <i>PHP</i> 3.0a1 is that while objects can reside inside
arrays, their properties cannot be directly referenced inside the arrays.
For example, you can do:

	$a[0] = $obj;

But you cannot reference to $a[0]'s properties using:

	$a[0]->...

This will be implemented at a later time.

<font size=+1><b><i>[7] Function pointers are now supported.
</i></b></font>
A simple illustrative example:

	$func_ptr = "time";
	$current_time = $func_ptr();

is identical to

	$current_time = time();

<font size=+1><b><i>[8] Indirect references are much more powerful.
</i></b></font>
For example, one can use the dollar operator an infinite amount of times:

	$a = "b";
	$b = "c";
	$c = "d";
	$d = "e";
	$e = "Testingn";

	echo $$$$$a;

Would display $e's content, which is "Testingn".

In addition, one can use complex expressions to generate variable names
using a perl-like notation:

	$i="123";
	${"test".$i} = 5;

would assign 5 to $test123.

<font size=+1><b><i>[9] A string concatenation operator was added.
</i></b></font>
A perl-like string concatenation operator was added, the dot operator.
It converts both of its arguments to strings, and concatenates them.
For example:

	$result = "abcd".5;

assigns "abcd5" to result.  Note that under <i>PHP</i> 3.0, if you were
to use the plus operator:

	$result = "abcd"+5;

$result would be set to 5 - as mentioned earlier, if one argument is a
string and the other is an integer, the string is converted to an integer,
which in this case results in 0, plus 5 - result is 5.


<font size=+1><b><i>[10] Supports passing function arguments by references instead of by value.
</i></b></font>
Support for passing function arguments by reference instead of by value
has been added.  This doesn't result in having to change the function
implementations in any way, but, when calling the function, you can
decide on whether the variable you supply would actually be changed by
the function, or a copy of it.

Example:

	function inc($arg)
	{
		$arg++;
	}

	$i=0;
	inc($i);  /* here $i in the outer scope wouldn't change, and remain 0 */
	inc(&$i);  /* here $i is passed by reference, and would change to 1 */


<font size=+1><b><i>[11] Support for multidimensional arrays.
</i></b></font>
(Or as Andi calls them, 'hyperdimensional variables'.)

The easiest way to define this support of <i>PHP</i> 3.0 is inductive -
arrays can contain any type of variables, including other arrays.
A simple example:

	$a[0]=5;
	$a[1]["testing"]=17;
	$b["foo"]=$a;

Ok, so it may be not so simple.  Play with it, it's pretty powerful.


<font size=+1><b><i>[12]	Array initialization is now supported.
</i></b></font>
	For example, let's say you want to initialize a lookup table to convert
	number to month names:

		$months = array("January", "February", "March",
						"April", "May", "June", "July", "August",
				 		"September", "October", "November", "December");

	would assign $months[0] to be January, $months[1] to be February, etc.
	Alternately, you may want the count to start at '1' instead of 0.
	You can do so easily:

		$months = array(1=>"January", "February", "March",
						"April", "May", "June", "July", "August",
						"September", "October", "November", "December");

	Also, you can specify an index for every entry, not just the first one:

		$first_names = array("Doe"=>"John", "Gates"=>"William",
							"Clinton"=>"Bill" });

	would assign $first_names["Doe"]="John", etc.


<font size=+1><b><i>[13]	Perl style lists now supported.
</i></b></font>
	Multiple values from arrays may now be assigned into several
	variables using one assignment.  For example:
	
		$str = "johndoe:x:555:555:Doe, John:/home/johndoe:/bin/tcsh";
		
		list($username,$passwd,$uid,$gid,$realname,$homedir,$shell) = 
			explode(":",$str);
	
	Would assign 'johndoe' into $username, 'x' into $passwd, etc.


<font size=+1><b><i>[14] Colons are supported in 'case' and 'default' statements.
</i></b></font>
For example:

	switch($value) {
	case 'A':
		statement;
		break;
	case 'B':
		statement;
		break;
	case 'C':
		statement;
		/* fall-through */
	default:
		statement;
	}


<h2>Non Language Related New Features</h2>

<font size=+1><b><i>[1] Persistent resource lists.
</i></b></font>
In plain english this means that there's now an easy way of writing the
SQL drivers so that they don't open and close the SQL link every time,
but instead open it the first time it's required, and then use it on
every later hit.  As of <i>PHP</i> 3.0a1, only the MySQL, mSQL and PostgresSQL
drivers have been changed (rewritten) to take advantage of this option.
To use it, use mysql_pconnect() instead of mysql_connect() (or the
equivalents for the two other databases).

<font size=+1><b><i>[2] Configuration file.
</i></b></font>
<i>PHP</i> now has its own configuration file, and many compile-time options
of <i>PHP</i>2 are now configurable at runtime.

<font size=+1><b><i>[3] Syntax Highlighting.
</i></b></font>
A syntax highlighter has been built into <i>PHP</i> 3.0, which means <i>PHP</i> 3.0 can
display your code, syntax highlighted, instead of executing it.  Right
now, it's only easy to do this by telling apache to execute a certain
extension (e.g., .php) and syntax highilghting another extension (e.g.,
.phps).  At a future version, we'll probably add display_source(filename)
which works like include(), only it displays the syntax highlighted
source instead of executing the included code.  At this time, this is
only available in the Apache version, and not in the CGI version.

<font size=+1><b><i>[4] Loadable modules.
</i></b></font>
This would have a huge impact on the Windows version, and would probably
be used in the UNIX environment as well.  One can now add <i>PHP</i> internal
functions in runtime by loading a dynamic module.  This is known to work
under Solaris, Linux and Win32 at this time, but would be ported to any
other capable platform if an incompatability is found.

<h2>Other Interesting Issues</h2>

<font size=+1><b><i>[1] Improved performance.
</i></b></font>
The performance of <i>PHP</i> 3.0 is much better than the one of <i>PHP</i> 2.0.
Memory consumption has been dramatically reduced in many cases, due
to the use of an internal memory manager, instead of apache's pools.
Speedwise, <i>PHP</i> 3.0 is somewhere between 2 and 3 times faster than <i>PHP</i> 2.0.


<font size=+1><b><i>[2] More reliable parser.
</i></b></font>
After <i>PHP</i> 3.0 is well tested, it'll be pretty safe to say that it's
more reliable than <i>PHP</i> 2.0 is.  While <i>PHP</i> 2.0 performed well on simple,
and fairly complex scripts, a fundamental design difference from <i>PHP</i> 3.0
makes it more prone to errors.  In <i>PHP</i> 3.0, obscure parser problems are
much less likely.

<font size=+1><b><i>[3] Improved C API.
</i></b></font>
If you're a C coder, adding functionality to <i>PHP</i> was never easier.
A pretty well documented API is available (apidoc.txt), and you no longer
have to touch the parser or scanner code when adding your function.
Also, it's more complicated to 'go wrong' when implementing a <i>PHP</i>3
function than it was in <i>PHP</i>2 (no stack to maintain) - but of course,
you can mess up here too :)

<font size=+1><b><i>[4] Name change.
</i></b></font>
<i>PHP</i>/<i>FI</i> 2.0 was renamed to <i>PHP</i> 3.0, and the meaning has changed from
'Personal Home Pages / Forms Interpreter' to '<i>PHP</i>: Hypertext Preprocessor'.
'Personal' home pages was an understatement for <i>PHP</i>/<i>FI</i> 2.0, and is
definitely an understatement for <i>PHP</i> 3.0.
</PRE></body></html>
