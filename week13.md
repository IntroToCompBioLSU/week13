# Week 13 Outline


## Plotting

- `matplotlib` is the most commonly used library for making scientific figures
  - NOTE: Some of the official `matplotlib` documentation is out of date
  - For help, it's best to look for up-to-date tutorials

- If you haven't already, [install `matplotlib`](https://matplotlib.org)

- We'll also use `numpy` today, so you should have that installed already.
  - It would also be a good idea to become familiar with [numpy arrays](https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html)

- For almost all the plotting you'll do, you only need this `import` line at the top

        import matplotlib.pyplot as plt

- `matplotlib` uses a hierarchy of elements in the figure that can be manipulated independently.

![matplotlib figure hierarchy](https://files.realpython.com/media/fig_map.bc8c7cabd823.png)

- `Figure` denotes the entire plotting areas

- An `Axes` is a subplot within a figure.

- Each `Axes` then has a bunch of elements that can be adjusted individually.

![matplotlib figure elements](https://files.realpython.com/media/anatomy.7d033ebbfbc8.png)

- There are different ways to interact with and adjust plots, but we'll use what's called the "object-oriented approach". Basically this just means that we keep track of and interact with each element of a plot individually. To adjust an element, we call some method associated with that element.

- Let's walk through this example taken from the Real Python site.

        import numpy as np
        import matplotlib.pyplot as plt

        # Look up the numpy documentation. What are these functions doing?
        rng = np.arange(50)
        rnd = np.random.randint(0, 10, size=(3, rng.size))
        yrs = 1950 + rng

        # What's going on here? What is the .subplots() function returning?
        # What is the figsize argument setting?
        fig, ax = plt.subplots(figsize=(5, 3))

        # This is a fake dataset, but how is it using the values generated with numpy?
        ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])

        # What sorts of plot elements are we setting?
        ax.set_title('Combined debt growth over time')
        ax.legend(loc='upper left')
        ax.set_ylabel('Total debt')
        ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])

        # What is this doing?
        fig.tight_layout()

        # Actually displays figure
        plt.show()

- What if you want to create a figure with more than one subplot?

        fig, ax = plt.subplots(2,2)
        # What does ax look like after this function call?

        ax[0,0].stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
        ax[0,1].stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
        ax[1,0].stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
        ax[1,1].stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])

        plt.show()

- What are some of the built-in plot types in `pyplot`?
  - Example plots: https://matplotlib.org/tutorials/introductory/sample_plots.html

        Pick two plot types from this gallery, figure out how to plot them, and
        create a figure with both plots on it.

## Matplotlib Resources

- [Real Python - Matplotlib Guide](https://realpython.com/python-matplotlib-guide/)

- [Official Matplotlib Information](https://matplotlib.org)

- [Nicolas Rougier's Matplotlib Tutorial](https://www.labri.fr/perso/nrougier/teaching/matplotlib/)


## Weekly Assignment

        - Use `matplotlib` to create some plot that we did not cover in class.
          - Try to find a plot that will be relevant to your final project.

        - Create a pseudocode outline for the overall structure of your final project.

        - Start filling out as much code as possible under your pseudocode outline. Flag areas where you are stuck or aren't quite sure how to proceed.


## NumPy Arrays

- Numpy arrays are specialized data structures for storing and manipulating multi-dimensional sets of values. Note that we've done some simples versions of this with lists of lists, but these lack any associated methods.

- Here's how we stored a 2-dimensional array using just standard Python lists

        myBasicArray = [[3,5,8],[9,12,14]]

- Here's the syntax to access the number in "row 2, column 2"

        myBasicArray[1][1]

- Here's our list-of-lists array printed to screen

        print(myBasicArray)

- However, if we want to do anything other than access or change these values, we would need to write custom functions to do so.

- Here's how we could store these same values as a numpy array. Remember that we still need to precede numpy functions with `np`. Note that the `array()` function requires a _single_ list as an argument.

        import numpy as np
        myArray = np.array([[3,5,8],[9,12,14]])

- We start to notice differences from lists of lists as soon as we print our array.

        print(myArray)

- Conveniently, numpy prints out the array in a matrix-like way.

- There are some built-in functions to create numpy arrays with either all 0s or all 1s, or a range of values.

        myAllZeroArray = np.zeros( (3,5) )
        print(myAllZeroArray)

        myAllOneArray = np.ones( (5,3) )
        print(myAllOneArray)

        myRangeArray = np.linspace(2,11.5,20)
        print(myRangeArray)

        # linspace gives a specified number of values in the given interval

- Now, let's say that we want to turn our one-dimensional array into an multi-dimensional array. Conveniently, numpy arrays have a built-in function to do this - called reshape().

        myRangeArray = myRangeArray.reshape( 2,10 )
        print( myRangeArray )
        myRangeArray = myRangeArray.reshape( 4,5 )
        print( myRangeArray )

- Multi-dimensional arrays can also easily be transformed. For instance, let's say we want to flip an array along its left-to-right axis.

        myRangeArray = np.fliplr(myRangeArray)
        print( myRangeArray )

- The power of numpy arrays becomes immediately apparent if we want to transform all the values in our array in some way. For instance, let's say we want to subtract a constant value from every element. All we have to do is write the operation with the array.

        print( myRangeArray-1 )
        print( myRangeArray*2 )
        print( myRangeArray**2 )

- These operations would not be possible as written with our basic list-of-lists array.

        myBasicArray-1  # Fail

- You can also evaluate boolean statements on all elements in an array.

        print( myRangeArray % 2 == 0 )  # Find even numbers

- Built-in functions are also available that operate on all elements of an array.

        print( myRangeArray.sum() )
        print( myRangeArray.min() )

- Array axes can be indexed independently to extract particular sets of values. For instance, let's say we want all values in the 3rd column.

        print( myRangeArray[ : , 2] )

- Multiple numpy arrays can be combined in different ways. For instance, if we wanted to stack arrays on top of one another, we can use the vstack() function.

        print( np.vstack( (myAllZeroArray,myAllOneArray.reshape(3,5)) ) )

## Drawing random numbers with NumPy

### Populations and Samples

- [Populations versus Samples - 365 Data Science - YouTube](https://www.youtube.com/watch?v=eIZD1BFfw8E)

- A _population_ consists of all members of a given set (e.g., all LSU students). We often want to understand something about a population (e.g., amount of student debt), but it can be very difficult (impossible) and time consuming to get this information from everyone. Instead, we take a _sample_ from this population, calculate the _statistic_ of interest for the sample, and use it to try and understand the population as a whole.

- Ideally, the _sample_ is randomly drawn from the entire population. The more members of the population are included in the sample, the more confident we can be that our _sample statistic_ accurately reflects the entire population. But just how much uncertainty is there in our estimate for a given sample size? This is a fundamental question in the field of statistics.

- If we know that the quantity of interest in the population has a certain distribution (e.g., Normal), we can sometimes just apply a known formula to tell us how confident we should be. But when the underlying distribution in the population is unknown, we rely on a procedure called _bootstrapping_.

### Bootstrapping

- One of the simplest and most useful things we can do with (pseudo-)random numbers is draw values from a dataset.

- We can draw these values in two ways - with or without replacement. If we sample _without_ replacement, we are just reordering the dataset. Each time we sample a value, we cannot sample it again.

        data = np.array([ 0.82803637,  0.00382416,  0.07481507,  0.99684717,  0.99995017,
                          0.63965781,  0.99360978,  0.3625829 ,  0.99999972,  0.98201947,
                          0.00118308,  0.52392163,  0.95489943,  0.45001676,  0.65437422,
                          0.94684642,  0.0114679 ,  0.94362976,  0.0704053 ,  0.27266416])
        data = np.random.choice(data, size=20, replace=False)
        print(data)
        data = np.random.choice(data, size=20, replace=False)
        print(data)

        # In these cases, each value in the original dataset is only present
        # once in the resampled datasets.

- When we sample _with_ replacement, some values may be sampled multiple times and others sampled not at all. Replacement means that when we sample a value, we put it back into the pool with the potential to be sampled again.

        print( np.random.choice(np.array([1,2,3,4,5]), size=5, replace=True) )
        print( np.random.choice(np.array([1,2,3,4,5]), size=5, replace=True) )
        print( np.random.choice(np.array([1,2,3,4,5]), size=5, replace=True) )
        print( np.random.choice(np.array([1,2,3,4,5]), size=5, replace=True) )
        print( np.random.choice(np.array([1,2,3,4,5]), size=5, replace=True) )

- One application of sampling with replacement is a procedure called "bootstrapping". The name comes from the phrase "pull yourself up by your bootstraps" and applies when we are trying to learn something about data drawn from an unknown distribution. To start, let's take a look at our data...

        import matplotlib.pyplot as plt
        plt.hist(data)
        plt.show()

- Now, let's say we're interested in learning about the mean of the population from which we've sampled these values

        dataMean = np.mean(data)
        print( dataMean )

- The data don't obviously come from a standard distribution, so it's difficult to know how confident we should be in our estimate of the mean. Bootstrapping is one way around this. We can draw a series of samples with replacement from our data and calculate their means. This collection of means gives us an idea of how confident we can be in our estimate.

        # Number of bootstrap replicates - more is better, but takes longer
        bootNumber = 100

        # array to store results of bootstrapping
        meanBoots = np.array([])

        # For loop to perform bootstrapping
        for _ in range(bootNumber):

            # Draw new bootstrap replicate
            samp = np.random.choice(data, size=data.size, replace=True)

            # Calculate mean from each replicate
            meanBoots = np.append(meanBoots,np.mean(samp))

        # Examine bootstrap distribution on the mean
        plt.hist(meanBoots)
        plt.show()

        # Sort the bootstrapped means
        meanBoots = np.sort(meanBoots)

        # We often use the 95% confidence interval as a measure of uncertainty

### Probability Distributions

#### Discrete Distributions

- Discrete Uniform

- Bernoulli

- Binomial

- Poisson

- Geometric

#### Continuous Distributions

-

#### Distribution Resources

- [Seeing Theory - Probability Distributions](https://seeing-theory.brown.edu/probability-distributions/index.html)
- [Wikipedia - Bernoulli](https://en.wikipedia.org/wiki/Bernoulli_distribution)
- [Wikipedia - Binomial](https://en.wikipedia.org/wiki/Binomial_distribution)
- [Wikipedia - Poisson](https://en.wikipedia.org/wiki/Poisson_distribution)
- [Wikipedia - Geometric](https://en.wikipedia.org/wiki/Geometric_distribution)
