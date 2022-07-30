set nf [molinfo top get numframes]

set asel_prot [atomselect top "((chain A and ((resid 149 to 151) or (resid 176 to 180) or (resid 212 to 219) or resid 245)) or (chain B and ((resid 119 164 166) or (resid 121 to 124) or (resid 157 to 158) or (resid 214 to 220) or (resid 250 to 253) or (resid 311 313 314)))) and name CA" frame 0]
set asel_lig [atomselect top "chain Z and noh" frame 0]

for {set i 0} { $i < $nf} {incr i} {
       molinfo top set frame $i
       set bsel_prot [atomselect top "((chain A and ((resid 149 to 151) or (resid 176 to 180) or (resid 212 to 219) or resid 245)) or (chain B and ((resid 119 164 166) or (resid 121 to 124) or (resid 157 to 158) or (resid 214 to 220) or (resid 250 to 253) or (resid 311 313 314)))) and name CA"]
       set tm [measure fit $bsel_prot $asel_prot]
       set all [atomselect top all]
       $all move $tm
       set bsel_lig [atomselect top "chain Z and noh"]
       set rmsd [measure rmsd $asel_lig $bsel_lig]
       $bsel_prot delete
       $bsel_lig delete
       $all delete
       puts "$i $rmsd"
}

$asel_prot delete
$asel_lig delete

       
