import unittest

from . import utils


class ScriptTest(unittest.TestCase, utils.ScriptsCommonTest):

    def __init__(self, *args, **kwargs):
        super(ScriptTest, self).__init__(*args, **kwargs)
        utils.ScriptsCommonTest.set_test_data()
        self.script_name = 'calc_wmetric.py'

    def test_arg_matrix_when_no_fasta(self):
        args = ['--matrix', 'blosum62']
        returncode, out = utils.runscript(self.script_name, args)
        self.assertEqual(returncode, 2)
        self.assertIn('--fasta/-f', out)

    def test_arg_matrix_invalid_choice(self):
        args = ['--matrix', 'nonexistent']
        returncode, out = utils.runscript(self.script_name, args)
        self.assertEqual(returncode, 2)
        self.assertIn('--matrix/-m', out)

    def test_output_default(self):
        args = ['--fasta', self.filename_pep]
        returncode, out, md5 = self._test_output(self.script_name, args)
        self.assertEqual(returncode, 0)
        self.assertEqual(md5, '27ad675a7a2e5c2872a8ab495f2d4494')

    def test_output_phylip(self):
        args = ['--fasta', self.filename_pep, '--outfmt', 'phylip']
        returncode, out, md5 = self._test_output(self.script_name, args)
        self.assertEqual(returncode, 0)
        self.assertEqual(md5, '27ad675a7a2e5c2872a8ab495f2d4494')

    def test_output_pairwise(self):
        args = ['--fasta', self.filename_pep, '--outfmt', 'pairwise']
        returncode, out, md5 = self._test_output(self.script_name, args)
        self.assertEqual(returncode, 0)
        self.assertEqual(md5, '195fb45ed46a80473e1d004b9ce40e94')

    def test_output_pam250(self):
        args = ['--fasta', self.filename_pep, '--outfmt', 'phylip',
                '--matrix', 'pam250']
        returncode, out, md5 = self._test_output(self.script_name, args)
        self.assertEqual(returncode, 0)
        self.assertEqual(md5, '217ed91de43b091205add32a673cf8fe')


if __name__ == '__main__':
    unittest.main()
