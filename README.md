# 4D Projections

This is a small little test script for projection 4D
[simplices](https://en.wikipedia.org/wiki/Simplex) onto a 2D rendering surface.
This was the prototype for my corresponding
[animation](https://chirprush.github.io/animations/animations/simplices/index.html),
so much of the code is structurally quite similar.

## A Brief Overview of the Math

For the purposes of this project, we're only interested in the vertices and the
edges of a single 4D object centered around $(0, 0)$, so this simplifies the
math quite a bit.

Suppose we have a set of ordered vertices $V \subset \mathbb{R}^n$ and edges $E
\subseteq V \times V$. We can then define a hyperplane with the equation $x_n =
-p$ and our viewpoint, or camera, to be at a position $c = (0,0,\ldots,0,-\ell)$.
Our projection is rather simple in that we simply extend a line from our camera
to each of the vertices $v \in V$ and find the unique point in which it
intersects our hyperplane. Formally, we parametrize the line $(v - c)t + c$ for
$0 \le t \le 1$, and then solve for $t$ knowing that the $n$th component of the
vector must be equal to the hyperplane value:
$$(v_n - c_n)t + c_n = -p \implies t = \frac{\ell + p}{c_n - v_n}.$$
Plugging this $t$ value back into the line gives the projected point.

This will take all our points in $n$ dimensional space and put them in $n - 1$
dimensional space as desired. I do believe that this doesn't quite preserve
"volume," but for my purposes (mainly just curiosity) that is fine.

## Output

The program will output to `stdout` a LaTeX file consisting of solely a
tikzpicture. One can compile this and then view it in any PDF viewer.
