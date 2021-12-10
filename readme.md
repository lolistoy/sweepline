# Sweep Line Algorithm for Segments Intersection

The problem here is simple: given a list of `N` segments,
find all intersections between pairs of segments.

Although it sounds quite straightforward to implement an `O(N^2)` algorithm for this, 
there is indeed better sweep line algorithms with `O(NlogN)` time complexity. 
This implementation takes both approaches and follows the [classic](#Reference).

![image](image.svg)

## Usage
The code depends on [sortedcontainers](http://www.grantjenks.com/docs/sortedcontainers/) 
and [gmpy2](https://gmpy2.readthedocs.io/en/latest/).
```python
import sweepline
segments = [((0, 0), (10, 10)), (5, -5), (5, 5)]
ret = sweepline.isect_segments(segments)
```
Or run the test(borrowed from [here](https://github.com/ideasman42/isect_segments-bentley_ottmann))
to see the algorithm in action

```
$ USE_ROTATION=1;USE_INCLUDE_ENDPOINTS=1 python3 -m unittest test.tests
```

## Details
The idea of the algorithm is pretty simple from [classic](#reference). However, several details need 
special care:

- When there are horizontal segments, the algorithm needs to treat them differently when the sweep line 
  sweeps before, in the middle and after sweeping the event relating to the segment.
- Degenerate segments(points) don't need to go into the tree.
- Duplicate segments need to be treated as different instances.
- Native `float` can have precision problem, multi-precision rationals `mpq` from `gmpy2` is used, because all 
  operations needed can be represented with rational numbers.
- The tree data structure from the algorithm to maintain current segments being swept is a
  specialized binary search tree. However, the comparator function is changing with the current event point.
  This is implemented with `sortedcontainer` with mutable comparator [function](https://github.com/lolistoy/sweepline/blob/9d120d72ce2121423bf464a07eb9e40b9a2fe613/sweepline.py#L56).  

## License
MIT License

## TODO
- Implement a C++/Cython version of this
- Benchmark for speed

## Reference
- Mark, de Berg, et al. Computational geometry algorithms and applications. Spinger, 2008.

- The test samples and code are based on the nice [repo](https://github.com/ideasman42/isect_segments-bentley_ottmann). 