import matplotlib.pyplot as plt
import matplotlib
import numpy as np

if __name__ == '__main__':
    # Pie: Male / Female
    font = {'family': 'arial',
            'size': 24}
    matplotlib.rcParams['mathtext.rm'] = 'arial'
    matplotlib.rc('font', **font)
    ##################################################################
    # Pie: Gender
    ##################################################################
    labels = 'Male', 'Female'
    sizes = [38, 40]
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    # fig1, ax1 = plt.subplots(figsize=[6.0, 6.0])
    fig1 = plt.figure(figsize=[6.0, 6.0])
    ax1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=45)
    plt.title("Gender")
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig("gender.png", dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.2,
                frameon=None, metadata=None)
    plt.show()

    ##################################################################
    # Pie: Age
    ##################################################################

    font = {'family': 'arial',
            'size': 24}
    matplotlib.rcParams['mathtext.rm'] = 'arial'
    matplotlib.rc('font', **font)
    labels = '<20', '20-29', '30-39', '>40'
    sizes = [8, 44,21,5]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    # fig1, ax1 = plt.subplots(figsize=[6.0, 6.0])
    fig1 = plt.figure(figsize=[6.0, 6.0])
    ax1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=0)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Ages")
    plt.savefig("gender.png", dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.2,
                frameon=None, metadata=None)
    plt.show()
    ##################################################################
    # Pie: Region
    ##################################################################
    font = {'family': 'arial',
            'size': 24}
    matplotlib.rcParams['mathtext.rm'] = 'arial'
    matplotlib.rc('font', **font)
    labels = 'Domestic', 'Non-Do.'
    sizes = [32, 46]
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    # fig1, ax1 = plt.subplots(figsize=[6.0, 6.0])
    fig1 = plt.figure(figsize=[6.0, 6.0])
    ax1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=45)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Region")
    plt.savefig("english.png", dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.2,
                frameon=None, metadata=None)
    plt.show()