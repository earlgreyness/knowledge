# Ubuntu 16.04 and NVIDIA GeForce GTX 550 Ti

To add latest open source drivers to apt, issue these commands:

    sudo apt-add-repository ppa:graphics-drivers/ppa
    sudo apt-get update

Go to *Applications/Additional Drivers* and enable the latest NVIDIA **open source** driver.

To get rid of vsync issues, run this command:

    nvidia-settings --assign CurrentMetaMode="nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On }"

If you want to apply this permanently, do the following:

    sudo nvidia-xconfig
    sudo nano /etc/X11/xorg.conf

You must achieve the following:

    Section "Device"
        Identifier     "Device0"
        Driver         "nvidia"
        VendorName     "NVIDIA Corporation"
        Option         "RegistryDwords" "PerfLevelSrc=0x3322; PowerMizerDefaultAC=0x1"
        Option         "TripleBuffer" "True"
        Option         "TearFree" "True"
    EndSection

    Section "Screen"
        Identifier     "Screen0"
        Device         "Device0"
        Monitor        "Monitor0"
        DefaultDepth    24
        SubSection     "Display"
            Depth       24
        EndSubSection
        Option "metamodes" "nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On }"
    EndSection

Only the `Option "metamodes"` part is mandatory. `Section "Device"` may be left intact. Try commenting out different options for best results.

After some experimentation, it seems like commenting out the `Option "metamodes"` part while having others remain gives the best performance.

