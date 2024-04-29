debImport "test.fsdb"
wvCreateWindow
wvSetPosition -win $_nWave2 {("G1" 0)}
wvOpenFile -win $_nWave2 {/nfs/home/zhaotiankun/workspace/ChipTest/test.fsdb}
wvGetSignalOpen -win $_nWave2
wvGetSignalSetScope -win $_nWave2 "/Passthrough"
wvSetPosition -win $_nWave2 {("G1" 5)}
wvSetPosition -win $_nWave2 {("G1" 5)}
wvAddSignal -win $_nWave2 -clear
wvAddSignal -win $_nWave2 -group {"G1" \
{/Passthrough/clock} \
{/Passthrough/io_in\[3:0\]} \
{/Passthrough/io_out\[3:0\]} \
{/Passthrough/regOut\[3:0\]} \
{/Passthrough/reset} \
}
wvAddSignal -win $_nWave2 -group {"G2" \
}
wvSelectSignal -win $_nWave2 {( "G1" 1 2 3 4 5 )} 
wvSetPosition -win $_nWave2 {("G1" 5)}
wvSetPosition -win $_nWave2 {("G1" 5)}
wvSetPosition -win $_nWave2 {("G1" 5)}
wvAddSignal -win $_nWave2 -clear
wvAddSignal -win $_nWave2 -group {"G1" \
{/Passthrough/clock} \
{/Passthrough/io_in\[3:0\]} \
{/Passthrough/io_out\[3:0\]} \
{/Passthrough/regOut\[3:0\]} \
{/Passthrough/reset} \
}
wvAddSignal -win $_nWave2 -group {"G2" \
}
wvSelectSignal -win $_nWave2 {( "G1" 1 2 3 4 5 )} 
wvSetPosition -win $_nWave2 {("G1" 5)}
wvGetSignalClose -win $_nWave2
wvZoomOut -win $_nWave2
wvZoomOut -win $_nWave2
wvZoomOut -win $_nWave2
wvZoomOut -win $_nWave2
wvZoomOut -win $_nWave2
wvZoomOut -win $_nWave2
wvZoomOut -win $_nWave2
wvZoomOut -win $_nWave2
wvSetCursor -win $_nWave2 73384.790186 -snap {("G1" 3)}
wvSetCursor -win $_nWave2 69643.604804 -snap {("G1" 4)}
wvSetCursor -win $_nWave2 62960.632626 -snap {("G1" 3)}
wvSetCursor -win $_nWave2 73640.597733 -snap {("G1" 3)}
wvSetCursor -win $_nWave2 61042.076019 -snap {("G1" 2)}
wvSetCursor -win $_nWave2 68620.374614 -snap {("G1" 3)}
wvSetCursor -win $_nWave2 15987.971718 -snap {("G1" 3)}
debExit
