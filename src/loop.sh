for j in {1..90}
do
for i in $(seq -f %03g $(3*n-2) $(3*n))
do
#python main.py
echo /home/jbgpl/seismic_DL/SR_denoising/SeismicSuperResolution/data/field/S08p08n$(i)_560x800.dat
done
done
#rm /home/jbgpl/seismic_DL/SR_denoising/SeismicSuperResolution/data/field/S08p08n${i}_560x800.dat
#rm /home/jbgpl/seismic_DL/SR_denoising/SeismicSuperResolution/data/field/S08p08n${i+1}_560x800.dat
#rm /home/jbgpl/seismic_DL/SR_denoising/SeismicSuperResolution/data/field/S08p08n${i+2}_560x800.dat
