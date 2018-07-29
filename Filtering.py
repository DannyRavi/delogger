from scipy.signal import lfilter, lfilter_zi, filtfilt, butter

class filtering:
    def __init__(self,order,freq ,dimens):
        self.order=order
        self.freq=freq
        self.dimen=dimens

        b, a = butter(order, freq ,analog=False)

        # Apply the filter to xn.  Use lfilter_zi to choose the initial condition
        # of the filter.
        zi = lfilter_zi(b, a)
        z, _ = lfilter(b, a, dimens, zi=zi*dimens[0])

        # Apply the filter again, to have a result filtered at an order
        # the same as filtfilt.
        z2, _ = lfilter(b, a, z, zi=zi*z[0])

        # Use filtfilt to apply the filter.
        yy = filtfilt(b, a, dimens)

        self.outy=abs(yy)
    
   
    