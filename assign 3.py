{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bdbd0dff",
   "metadata": {},
   "source": [
    "### processing data using Named Entity Recognition technique"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2d9441ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(S\n",
      "  State/UTs/NNP\n",
      "  ,/,\n",
      "  (PERSON Total/NNP Cases/NNP)\n",
      "  ,/,\n",
      "  (GPE Active/NNP)\n",
      "  ,/,\n",
      "  (GPE Discharged/NNP)\n",
      "  ,/,\n",
      "  (GPE Deaths/NNP)\n",
      "  ,/,\n",
      "  (PERSON Active/NNP Ratio/NNP)\n",
      "  ,/,\n",
      "  (PERSON Discharge/NNP Ratio/NNP)\n",
      "  ,/,\n",
      "  (PERSON Death/NNP Ratio/NNP)\n",
      "  ,/,\n",
      "  (ORGANIZATION Population/NNP Andaman/NNP)\n",
      "  and/CC\n",
      "  Nicobar,10747,0,10618,129,0.0,98.8,1.2,100896618/NNP\n",
      "  (PERSON Andhra/NNP)\n",
      "  Pradesh,2339078,7,2324338,14733,0.0,99.37,0.63,128500364/NNP\n",
      "  Arunachal/NNP\n",
      "  Pradesh,66891,0,66595,296,0.0,99.56,0.44,658019/NNP\n",
      "  Assam,746100,0,738065,8035,0.0,98.92,1.08,290492/NNP\n",
      "  Bihar,851404,1,839100,12303,0.0,98.55,1.45,40100376/NNP\n",
      "  Chandigarh,99358,3,98174,1181,0.0,98.81,1.19,30501026/NNP\n",
      "  Chhattisgarh,1177768,8,1163614,14146,0.0,98.8,1.2,28900667/NNP\n",
      "  Dadra/NNP\n",
      "  and/CC\n",
      "  (PERSON Nagar/NNP Haveli/NNP)\n",
      "  and/CC\n",
      "  (PERSON Daman/NNP)\n",
      "  and/CC\n",
      "  Diu,11591,0,11587,4,0.0,99.97,0.03,231502578/NNP\n",
      "  Delhi,2007313,10,1980781,26522,0.0,98.68,1.32,773997/NNP)\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "\n",
    "import nltk\n",
    "\n",
    "# read input data from file\n",
    "with open('covid.txt.csv', 'r') as f:\n",
    "    input_text = f.read()\n",
    "\n",
    "# tokenize the input text into sentences\n",
    "sentences = nltk.sent_tokenize(input_text)\n",
    "\n",
    "# loop through each sentence and perform named entity recognition\n",
    "for sentence in sentences:\n",
    "    words = nltk.word_tokenize(sentence)\n",
    "    tagged = nltk.pos_tag(words)\n",
    "    named_entities = nltk.ne_chunk(tagged)\n",
    "    print(named_entities)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a4bd5214",
   "metadata": {},
   "source": [
    "### processing data using stemming"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cb056e95",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Stemmed text:\n",
      "state/ut , total case , activ , discharg , death , activ ratio , discharg ratio , death ratio , popul andaman and nicobar,10747,0,10618,129,0.0,98.8,1.2,100896618 andhra pradesh,2339078,7,2324338,14733,0.0,99.37,0.63,128500364 arunach pradesh,66891,0,66595,296,0.0,99.56,0.44,658019 assam,746100,0,738065,8035,0.0,98.92,1.08,290492 bihar,851404,1,839100,12303,0.0,98.55,1.45,40100376 chandigarh,99358,3,98174,1181,0.0,98.81,1.19,30501026 chhattisgarh,1177768,8,1163614,14146,0.0,98.8,1.2,28900667 dadra and nagar have and daman and diu,11591,0,11587,4,0.0,99.97,0.03,231502578 delhi,2007313,10,1980781,26522,0.0,98.68,1.32,773997\n"
     ]
    }
   ],
   "source": [
    "import nltk\n",
    "from nltk.stem import PorterStemmer\n",
    "\n",
    "# initialize stemmer object\n",
    "stemmer = PorterStemmer()\n",
    "\n",
    "# read input data from file\n",
    "with open('covid.txt.csv', 'r') as f:\n",
    "    input_text = f.read()\n",
    "\n",
    "# tokenize the input text into words\n",
    "words = nltk.word_tokenize(input_text)\n",
    "\n",
    "# stem each word in the list\n",
    "stemmed_words = []\n",
    "for word in words:\n",
    "    stemmed_word = stemmer.stem(word)\n",
    "    stemmed_words.append(stemmed_word)\n",
    "\n",
    "# join the stemmed words back into a text string\n",
    "output_text = ' '.join(stemmed_words)\n",
    "\n",
    "# print the output texts\n",
    "\n",
    "print(\"\\nStemmed text:\")\n",
    "print(output_text)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cca4b433",
   "metadata": {},
   "source": [
    "### processing data using Lemmatization technique"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b6319944",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Lemmatized text:\n",
      "State/UTs , Total Cases , Active , Discharged , Deaths , Active Ratio , Discharge Ratio , Death Ratio , Population Andaman and Nicobar,10747,0,10618,129,0.0,98.8,1.2,100896618 Andhra Pradesh,2339078,7,2324338,14733,0.0,99.37,0.63,128500364 Arunachal Pradesh,66891,0,66595,296,0.0,99.56,0.44,658019 Assam,746100,0,738065,8035,0.0,98.92,1.08,290492 Bihar,851404,1,839100,12303,0.0,98.55,1.45,40100376 Chandigarh,99358,3,98174,1181,0.0,98.81,1.19,30501026 Chhattisgarh,1177768,8,1163614,14146,0.0,98.8,1.2,28900667 Dadra and Nagar Haveli and Daman and Diu,11591,0,11587,4,0.0,99.97,0.03,231502578 Delhi,2007313,10,1980781,26522,0.0,98.68,1.32,773997\n"
     ]
    }
   ],
   "source": [
    "\n",
    "import nltk\n",
    "from nltk.stem import WordNetLemmatizer\n",
    "\n",
    "# initialize lemmatizer object\n",
    "lemmatizer = WordNetLemmatizer()\n",
    "\n",
    "# read input data from file\n",
    "with open('covid.txt.csv', 'r') as f:\n",
    "    input_text = f.read()\n",
    "\n",
    "# tokenize the input text into words\n",
    "words = nltk.word_tokenize(input_text)\n",
    "\n",
    "# lemmatize each word in the list\n",
    "lemmatized_words = []\n",
    "for word in words:\n",
    "    lemmatized_word = lemmatizer.lemmatize(word)\n",
    "    lemmatized_words.append(lemmatized_word)\n",
    "\n",
    "# join the lemmatized words back into a text string\n",
    "output_text = ' '.join(lemmatized_words)\n",
    "\n",
    "# print the output texts\n",
    "\n",
    "print(\"\\nLemmatized text:\")\n",
    "print(output_text)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "71195129",
   "metadata": {},
   "source": [
    "### processing data using Text Enrichment/Augmentation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3a88e3bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('Andaman', 'NNP'), ('and', 'CC'), ('Nicobar', 'NNP')]\n",
      "[('Andhra', 'NNP'), ('Pradesh', 'NNP')]\n",
      "[('Arunachal', 'NNP'), ('Pradesh', 'NNP')]\n",
      "[('Assam', 'NN')]\n",
      "[('Bihar', 'NN')]\n",
      "[('Chandigarh', 'NN')]\n",
      "[('Chhattisgarh', 'NN')]\n",
      "[('Dadra', 'NNP'), ('and', 'CC'), ('Nagar', 'NNP'), ('Haveli', 'NNP'), ('and', 'CC'), ('Daman', 'NNP'), ('and', 'CC'), ('Diu', 'NNP')]\n",
      "[('Delhi', 'NN')]\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import nltk\n",
    "from nltk.tokenize import word_tokenize\n",
    "\n",
    "\n",
    "\n",
    "# Open CSV file and read contents\n",
    "with open('covid.txt.csv', 'r', encoding='utf-8' ) as file:\n",
    "    reader = csv.reader(file)\n",
    "    next(reader)  # Skip header row\n",
    "    for row in reader:\n",
    "        text = row[0]  # Assumes text data is in first column of CSV\n",
    "        tokens = word_tokenize(text)\n",
    "        tagged_tokens = nltk.pos_tag(tokens)\n",
    "        # Do something with tagged_tokens here\n",
    "        print(tagged_tokens)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d77c0bc9",
   "metadata": {},
   "source": [
    "### processing data using Normalization technique"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8f39f0c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Normalized text:\n",
      "stateutstotal casesactivedischargeddeathsactive ratiodischarge ratiodeath ratiopopulation andaman nicobar107470106181290098812100896618 andhra pradesh23390787232433814733009937063128500364 arunachal pradesh66891066595296009956044658019 assam74610007380658035009892108290492 bihar85140418391001230300985514540100376 chandigarh99358398174118100988111930501026 chhattisgarh11777688116361414146009881228900667 dadra nagar haveli daman diu115910115874009997003231502578 delhi200731310198078126522009868132773997\n"
     ]
    }
   ],
   "source": [
    "\n",
    "import nltk\n",
    "from nltk.stem import WordNetLemmatizer\n",
    "from nltk.corpus import stopwords\n",
    "import string\n",
    "\n",
    "# initialize lemmatizer object\n",
    "lemmatizer = WordNetLemmatizer()\n",
    "\n",
    "# read input data from file\n",
    "with open('covid.txt.csv', 'r') as f:\n",
    "    input_text = f.read()\n",
    "\n",
    "# remove punctuation marks\n",
    "input_text = input_text.translate(str.maketrans('', '', string.punctuation))\n",
    "\n",
    "# convert input text to lowercase\n",
    "input_text = input_text.lower()\n",
    "\n",
    "# tokenize the input text into words\n",
    "words = nltk.word_tokenize(input_text)\n",
    "\n",
    "# remove stop words\n",
    "stop_words = set(stopwords.words('english'))\n",
    "words = [word for word in words if word not in stop_words]\n",
    "\n",
    "# lemmatize each word in the list\n",
    "lemmatized_words = []\n",
    "for word in words:\n",
    "    lemmatized_word = lemmatizer.lemmatize(word)\n",
    "    lemmatized_words.append(lemmatized_word)\n",
    "\n",
    "# join the lemmatized words back into a text string\n",
    "output_text = ' '.join(lemmatized_words)\n",
    "\n",
    "# print the output texts\n",
    "print(\"\\nNormalized text:\")\n",
    "print(output_text)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
