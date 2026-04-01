'''Plotting bus ridership and fare collection on recent WMATA buses'''
import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("TotalBoardingsPaid.csv", delimiter=',', names=True, dtype=None)

yoymonth = [1,2,3,4,5,6,7,8,9,10,11,12]
yoytotal = 100*(data["TotalBoardings"][-12:] - data["TotalBoardings"][-24:-12])/data["TotalBoardings"][-24:-12]
yoypaid = 100*(data["TotalPaid"][-12:] - data["TotalPaid"][-24:-12])/data["TotalPaid"][-24:-12]

mommonth = [1,2,3,4,5,6,7,8,9,10,11,12]
momtotal = 100*(data["TotalBoardings"][-12:] - data["TotalBoardings"][-13:-1])/data["TotalBoardings"][-13:-1]
mompaid = 100*(data["TotalPaid"][-12:] - data["TotalPaid"][-13:-1])/data["TotalPaid"][-13:-1]

fig, ax = plt.subplots(1,3)
fig.suptitle("WMATA Bus Ridership and Fare Collection")
ax[0].bar(data["Month"], data["TotalBoardings"], label="Total")
ax[0].bar(data["Month"], data["TotalPaid"], label="Paid")
ax[0].legend(loc=0)
ax[0].set_xlim(42,91)
ax[0].set_xticks(ticks=[43,55,67,79,91],labels=["2022","2023","2024","2025","2026"])
ax[0].set_ylim(0,12e6)
ax[0].set_ylabel("Monthly Ridership (Millions)")
ax[0].set_yticks(ticks=[0,2e6,4e6,6e6,8e6,10e6,12e6],labels=["0","2","4","6","8","10","12"])
ax[0].set_title("Overall")

ax[1].bar(yoymonth, yoytotal, label="Total")
ax[1].bar(yoymonth, yoypaid, label="Paid", alpha=0.8)
ax[1].set_xlim(0.5,12.5)
ax[1].set_xticks(ticks=yoymonth, labels=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
ax[1].legend(loc=0)
ax[1].set_title("Year Over Year Change (%)")
ax[1].set_ylim(-20,30)

ax[2].bar(mommonth, momtotal, label="Total")
ax[2].bar(mommonth, mompaid, label="Paid", alpha=0.8)
ax[2].set_xlim(0.5,12.5)
ax[2].set_xticks(ticks=mommonth, labels=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
ax[2].legend(loc=0)
ax[2].set_title("Month Over Month Change (%)")
ax[2].set_ylim(-20,30)

fig.set_size_inches(18, 7)
#fig.set_dpi(100)
plt.tight_layout()
#plt.savefig("WMATABuses202512.png")

fig, bx = plt.subplots()
bx.set_title("WMATA Bus Ridership and Fare Collection (all dates)")
bx.bar(data["Month"], data["TotalBoardings"], label="Total")
bx.bar(data["Month"], data["TotalPaid"], label="Paid")
bx.legend(loc=0)
bx.set_xlim(0,91)
bx.set_xticks(ticks=[7,19,31,43,55,67,79,91],labels=["2019","2020","2021","2022","2023","2024","2025","2026"])
bx.set_ylim(0,12e6)
bx.set_ylabel("Monthly Ridership (Millions)")
bx.set_yticks(ticks=[0,2e6,4e6,6e6,8e6,10e6,12e6],labels=["0","2","4","6","8","10","12"])

fig.set_size_inches(18, 7)
#fig.set_dpi(100)
plt.tight_layout()
#plt.savefig("WMATABuses20182025.png")

plt.show()
