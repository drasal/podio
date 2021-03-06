import unittest
from EventStore import EventStore
import os

from ROOT import TFile

class EventStoreTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = 'example.root'
        self.assertTrue( os.path.isfile(self.filename) )
        self.store = EventStore([self.filename])
        
    def test_eventloop(self):
        self.assertTrue( self.store.getEntries() >= 0 )
        self.assertEqual( self.store.getEntries(), len(self.store) )
        for iev, event in enumerate(self.store):
            self.assertTrue( True )
            if iev>5:
                break

    def test_navigation(self):
        event0 = self.store[0]
        self.assertEqual( event0.__class__, self.store.__class__)

    def test_collections(self):
        evinfo = self.store.get("info")
        self.assertTrue( len(evinfo)>0 )
        particles = self.store.get("CollectionNotThere")
        self.assertFalse(particles)

    def test_chain(self):
        self.store = EventStore( [ self.filename,
                                   self.filename] )
        rootfile = TFile(self.filename)
        events = rootfile.Get('events')
        numbers = []
        for iev, event in enumerate(self.store):
            evinfo = self.store.get("info")
            numbers.append(evinfo[0].Number())
        self.assertEqual( iev+1, 2*events.GetEntries() )
        # testing that numbers is [0, .. 1999, 0, .. 1999]
        self.assertEqual(numbers, range(events.GetEntries())*2)
        # trying to go to an event in the second file
        self.assertRaises(ValueError, self.store.__getitem__,
                          events.GetEntries()+1)

    # def test_handles(self):
    #     assocs = self.store.get("GenJetParticle")
    #     particles = self.store.get("GenParticle")
    #     jets = self.store.get("GenJet")
    #     self.assertTrue( len(assocs)>0 )
    #     jet = assocs[0].Jet()
    #     ptc = assocs[0].Particle()
    #     self.assertIsNotNone( jet )
    #     self.assertIsNotNone( ptc )
    #     self.assertTrue( jet in jets )
    #     self.assertTrue( ptc in particles )
    #     self.assertFalse( jet in particles )
    #     self.assertFalse( ptc in jets )
    #     ptcsInJet0 = []
    #     for assoc in assocs:
    #         jet = assoc.Jet()
    #         if jet == jets[0]:
    #             ptcsInJet0.append( assoc.Particle() )
    #     self.assertTrue( len(ptcsInJet0) > 0)
                
            

if __name__ == "__main__":
    from ROOT import gSystem
    from subprocess import call
    import os 
    gSystem.Load("libTestDataModel")
    # creating example file for the tests
    if not os.path.isfile('example.root'):
        write = '{podio}/examples/write'.format(podio=os.environ['PODIO'])
        print write 
        call(write)
    unittest.main()

