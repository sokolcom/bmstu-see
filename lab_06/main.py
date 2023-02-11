import sys

from PyQt5.QtWidgets import QApplication

from cocomo.ui import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())





# import matplotlib.pyplot as plt

# plt.rcParams['savefig.facecolor'] = "0.8"

# def example_plot(ax, fontsize=12):
#      ax.plot([1, 2])
#      ax.locator_params(nbins=3)
#      ax.set_xlabel('x-label', fontsize=fontsize)
#      ax.set_ylabel('y-label', fontsize=fontsize)
#      ax.set_title('Title', fontsize=fontsize)

# plt.close('all')
# fig = plt.figure()

# fig.set_figheight(15)
# fig.set_figwidth(15)


# ax1 = plt.subplot2grid((3, 3), (0, 0))
# ax2 = plt.subplot2grid((3, 3), (0, 1), colspan=2)
# ax3 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)
# ax4 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)

# example_plot(ax1)
# example_plot(ax2)
# example_plot(ax3)
# example_plot(ax4)

# plt.tight_layout()
# plt.show()