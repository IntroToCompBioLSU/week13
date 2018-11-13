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


## Weekly Assignment

- Use `matplotlib` to create some plot that we did not cover in class.
  - Try to find a plot that will be relevant to your final project.

- Create a pseudocode outline for the overall structure of your final project.

- Start filling out as much code as possible under your pseudocode outline. Flag areas where you are stuck or aren't quite sure how to proceed.


## Resources

- [Real Python - Matplotlib Guide](https://realpython.com/python-matplotlib-guide/)
