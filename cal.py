#t1, t2
#(r1, phi1, theta1) and (r2, phi2, theta2)
import datetime

def collide(t1, t2, r1, phi1, theta1, r2, phi2, theta2)
	delta = t2-t1
	delta_seconds = delta.total_seconds()

	v = (r1-r2)/delta_seconds
	vrock = (r1-r0)/t1.timestamp()
	r0 = r1 - vrock * t1.timestamp()
    #r0 = r2 - v * t2

    mφ = (phi1 - phi2) / delta_seconds
    bφ = phi1 - mφ * t1.timestamp()
    #bφ = phi2 - mφ * t2

    mθ = (phi1 - phi2) / delta_seconds
    bθ = phi1 - mθ * t1.timestamp()
    #bθ = phi2 - mθ * t2

    vslug = 10.0

    tcollide = r0 / (vrock - vslug)
    phicollide = mφ * tcollide + bφ
    thetacollide = m0 * tcollide + b0

    return (tcollide,phicollide,thetacollide)
