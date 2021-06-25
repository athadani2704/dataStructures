<h2>612. Shortest Distance in a Plane</h2><h3>Medium</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div>Table <code>point_2d</code> holds the coordinates (x,y) of some unique points (more than two) in a plane.
<p>&nbsp;</p>
Write a query to find the shortest distance between these points rounded to 2 decimals.

<p>&nbsp;</p>

<pre>| x  | y  |
|----|----|
| -1 | -1 |
| 0  | 0  |
| -1 | -2 |
</pre>

<p>&nbsp;</p>
The shortest distance is 1.00 from point (-1,-1) to (-1,2). So the output should be:

<p>&nbsp;</p>

<pre>| shortest |
|----------|
| 1.00     |
</pre>

<p>&nbsp;</p>
<b>Note:</b> The longest distance among all the points are less than 10000.

<p>&nbsp;</p>
</div>