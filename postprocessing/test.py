import pandas as pd

from address_correction import AddressCorrection
address_correction = AddressCorrection()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, default='result.csv')
    parser.add_argument('--output_file', type=str, default='result_corrected.csv')
    args = parser.parse_args()
    return args

def correct(answer):
    if not answer:
        return ""
    answer = answer.lower()
    result, diff = address_correction.address_correction(answer, correct_th=40)
    result = result.replace(",", "")
    result = " ".join([x.capitalize() for x in result.split()])
    if result.strip()==answer:
        diff=0
    return result.strip(),#diff

def main():
    args = parse_args()
    input_file = args.input_file
    output_file = args.output_file
    df = pd.read_csv(input_file)
    df['answer'] = df['answer'].apply(lambda x: x if pd.notna(x) else '')
    # df['corrected_answer'], df['diff'] = zip(*df['answer'].apply(lambda x: correct(x)))
    df['answer']=df["answer"].apply(lambda x: correct(x))
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()