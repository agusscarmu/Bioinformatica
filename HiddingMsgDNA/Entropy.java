package HiddingMsgDNA;

public class Entropy {


    public static double calculateEntropy(String[] motifs) {
        int numMotifs = motifs.length;
        int motifLength = motifs[0].length();
        double entropy = 0;

        // Iterar a través de cada columna
        for (int i = 0; i < motifLength; i++) {
            // Contar la frecuencia de cada nucleótido en esta columna
            int countA = 0, countC = 0, countG = 0, countT = 0;
            for (int j = 0; j < numMotifs; j++) {
                char nucleotide = motifs[j].charAt(i);
                if (nucleotide == 'A') {
                    countA++;
                } else if (nucleotide == 'C') {
                    countC++;
                } else if (nucleotide == 'G') {
                    countG++;
                } else if (nucleotide == 'T') {
                    countT++;
                }
            }

            // Calcular la frecuencia de cada nucleótido como un porcentaje
            double freqA = (double) countA / numMotifs;
            double freqC = (double) countC / numMotifs;
            double freqG = (double) countG / numMotifs;
            double freqT = (double) countT / numMotifs;

            // Calcular la entropía de esta columna
            double columnEntropy = 0;
            if (freqA > 0) {
                columnEntropy -= freqA * log2(freqA);
            }
            if (freqC > 0) {
                columnEntropy -= freqC * log2(freqC);
            }
            if (freqG > 0) {
                columnEntropy -= freqG * log2(freqG);
            }
            if (freqT > 0) {
                columnEntropy -= freqT * log2(freqT);
            }

            // Agregar la entropía de esta columna a la entropía total
            entropy += columnEntropy;
        }

        return entropy;
    }

    // Método auxiliar para calcular el logaritmo base 2
    private static double log2(double x) {
        return Math.log(x) / Math.log(2);
    }

    public static void main(String[] args) {
        String[] motifs = {
            "TCGGGGGTTTTT",
            "CCGGTGACTTAC",
            "ACGGGGATTTTC",
            "TTGGGGACTTTT",
            "AAGGGGACTTCC",
            "TTGGGGACTTCC",
            "TCGGGGATTCAT",
            "TCGGGGATTCCT",
            "TAGGGGAACTAC",
            "TCGGGTATAACC"
        };

        double entropy = calculateEntropy(motifs);
        System.out.println("Entropía de la matriz de motivos: " + entropy);
    }
}


