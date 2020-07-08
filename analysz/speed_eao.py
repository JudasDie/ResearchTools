import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

from matplotlib.backends.backend_pdf import PdfPages
pdf = PdfPages('speed-eao2018.pdf')

plt.rc('font',family='Times New Roman')
plt.rcParams['xtick.direction'] = 'in' 
plt.rcParams['ytick.direction'] = 'in' 



trackers = ['C-RPN', 'SA-Siam', 'DaSiamRPN', 'ATOM', 'SiamRPN++', 'DiMP', 'Ours (offline-2)', 'Ours (offline-1)', 'Ours (online)', 'Ours (alex)', 'SiamRPN']

speed = np.array([32, 50, 70, 30, 35, 40, 70, 50, 25, 130, 210]) / 100
speed_temp = np.array([32, 50, 70, 30, 35, 40,  70, 50, 25, 130, 210]) 
performance = np.array([0.273, 0.236, 0.380, 0.401, 0.414, 0.440, 0.438, 0.467, 0.507, 0.344, 0.368]) 

# close = np.array([10, 40, 70, 100, 130, 160, 190, 240])
close_circle = ['cornflowerblue', 'deepskyblue',  'turquoise', 'gold', 'yellowgreen', 'orange', 'r', 'r', 'r', 'r', 'turquoise']
close_font = ['k'] * 11

# Marker size in units of points^2
volume = (150 * speed/5 * performance/0.6)  ** 2
# close =  255 * speed * performance


fig, (ax, ax2, ax3) = plt.subplots(1, 3, sharey=True)

ax.scatter(speed_temp, performance, c=close_circle, s=volume, alpha=0.4)
ax2.scatter(speed_temp, performance, c=close_circle, s=volume, alpha=0.4)
ax3.scatter(speed_temp, performance, c=close_circle, s=volume, alpha=0.4)

ax.set_xlim(20, 80)
ax2.set_xlim(120, 140)
ax3.set_xlim(200, 220)

ax.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)


# plt.xlim((20, 80))
plt.ylim((0.2, 0.55))



# puttext
plt.text(speed_temp[0] - 2.37, performance[0] - 0.027, trackers[0], fontsize=10, color=close_font[0], weight='heavy')
plt.text(speed_temp[1] - 2.45, performance[1] - 0.03, trackers[1], fontsize=10, color=close_font[1], weight='heavy')
plt.text(speed_temp[2] - 3, performance[2] - 0.06, trackers[2], fontsize=10, color=close_font[2], weight='heavy')
plt.text(speed_temp[3] - 2.5, performance[3] - 0.032, trackers[3], fontsize=10, color=close_font[3], weight='heavy')
plt.text(speed_temp[4] - 2.5, performance[4] - 0.035, trackers[4], fontsize=10, color=close_font[4], weight='heavy')
plt.text(speed_temp[5] - 1.8, performance[5] - 0.042, trackers[5], fontsize=10, color=close_font[5], weight='heavy')
plt.text(speed_temp[6] - 5, performance[6] + 0.055, trackers[6], fontsize=14, color=close_font[6], weight='heavy')
plt.text(speed_temp[7] - 4.5, performance[7] -0.052, trackers[7], fontsize=12, color=close_font[7], weight='heavy')
plt.text(speed_temp[8] - 4, performance[8] -0.035, trackers[8], fontsize=12, color=close_font[8], weight='heavy')


ax.set_xlabel('Tracking Speed (FPS)', fontsize=15)
ax.set_ylabel('EAO', fontsize=15)
ax.set_title('EAO $vs.$ Speed on VOT-2018', fontsize=15)



plt.xticks(fontsize=15)
plt.yticks(fontsize=15)




plt.grid(linestyle='-.')
fig.tight_layout()

plt.savefig('speed-eao2018.png', dpi=3000)


pdf.savefig()
pdf.close()
plt.show()
