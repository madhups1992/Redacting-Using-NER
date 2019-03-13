import argparse

import project1

def main(files,otherfile,concept,outfile,statfile):
    Directory = '/project/cs5293sp19-project1/project1'
    file_regexp = str('"')+files+str('"')
    if (file_regexp == "*.txt"|".txt"):
        filename , ls = read_textfiles_from_directory(Directory, file_regexp)
        redacted_file=[]
        stats=[]
        concept = 'thank'
        for i in range(len(ls)):
            redacted_file.append(redaction(ls[i],concept))
            stats.append(redation_summary(ls[i],concept))
        store_redactedfiles(redacted_file)
        Writing_statistics(stats,Directory+'/'+statfile+'.txt',filename)

    else:
        print("Mismatch type")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",type=str,required=True)
    parser.add_argument("--names",type=str,required=False)
    parser.add_argument("--datea",type=str,required=False)
    parser.add_argument("--addresses",type=str,required=False)
    parser.add_argument("--phones",type=str,required=False)
    parser.add_argument("--concept",type=str,required=True)
    parser.add_argument("--output",type=str,required=True)
    parser.add_argument("--stats",type=str,required=False)

    args = []
    args= parser.parse_args()
    for i in range(len(args)):
        if args[i].input:
            files = args.input
        if args[i].concept:
            concept = args.concept
        if args[i].output:
            outfile = args.output
        if args[i].stats:
            statfile = args.stats
    main(files,otherfile,concept,outfile,statfile)



