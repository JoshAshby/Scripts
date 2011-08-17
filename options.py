#Quick python hack for SL4A that gives a menu option for quickly getting to
#ConnectBot, Cyanogenmod settings, AutoProxy, or Droidwall
#JoshAshby 2011 joshuaashby@joshashby.com http://joshashby.com

import android
droid=android.Android()

options=["SSH", "Cyanogenmod settings","Firewall","Proxy"]
droid.dialogCreateAlert("Pick something...")
droid.dialogSetItems(options)
droid.dialogShow()
picked = droid.dialogGetResponse().result

if (picked['item'] == 0):
	#pring "SSH"
	droid.makeToast("Starting Connectbot SSH client...")
	droid.startActivity(None,None,None,None,True, "org.woltage.irssiconnectbot", "org.woltage.irssiconnectbot.HostListActivity")
elif (picked['item'] == 1):
	#print "Cyanogenmod settings"
	droid.makeToast("Starting Cyanogenmod Settings...")
	droid.startActivity(None,None,None,None,True,"com.cyanogenmod.cmparts","com.cyanogenmod.cmparts.activities.MainActivity")
elif (picked['item'] == 2):
	#print "Firewall"
	droid.makeToast("Starting Droidwall firewall settings...")
	droid.startActivity(None,None,None,None,True,"com.googlecode.droidwall.free", "com.googlecode.droidwall.free.MainActivity")
elif (picked['item'] == 3):
	#print "Proxy"
	droid.makeToast("Starting AutoProxy proxy settings...")
	droid.startActivity(None,None,None,None,True,"net.moronigranja.tproxy", "net.moronigranja.tproxy.ProxyListActivity")
else:
	#print "Fail"
	droid.makeToast("Failed for some reason...")
	pass
exit()
