# Scaled Sleep Sort


Sleep sort is a sorting algorithm that as the name suggests makes a thread sleep for the value of each item in a list. 

However sorting like this will take as long as `k` the largest number in the list, or `O (k)`. 

But in this project I explore scaling the values of the list down to reduce the sleep time to a few seconds.

## Logarithmic scaling (base 10)

This was the initial idea and showed promise. Unfortunately there is a minimum time that a thread can be put to sleep pratical limitations. This causes irregularities as seen below. 

<p align="center">
  <img src="https://github.com/andibakti/scaledsleepsort/blob/master/log-chart.JPG"/>
</p>

Probable culprits:
* `time.sleep()` is reliable to within 10 - 15 milliseconds anything smaller will be inconsistent
* Threads that are started earlier get an advantage over others


## Linear scaling

One alternative to log scaling is linear scaling he list is scaled linearly using the constant `0.0135`.
This imposes a scrict limit of 13.5 milliseconds between threads and could theoretically fix the previous issue.

<p align="center">
  <img src="https://github.com/andibakti/scaledsleepsort/blob/master/linear-chart.JPG"/>
</p>


## Improvements

* Added a static variable to make all threads start at the same time: 
    Similar results where found (under the hood it might still be starting them one at a time due to the `while` loop).
* Since the list is almost sorted, **insertion sort** works best and overcomes the errors of sleep sort.


## Conclusion

    Good idea... in theory.
