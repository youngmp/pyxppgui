# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import sys
import time
import gc
import matplotlib
import wx
import wx.xrc
import os
matplotlib.use('WXAgg')
import matplotlib.cm as cm
import matplotlib.cbook as cbook
from matplotlib.backends.backend_wxagg import Toolbar, FigureCanvasWxAgg
from matplotlib.figure import Figure
import numpy as np

from xppcall import xpprun, read_pars, read_inits, read_numerics

###########################################################################
## Class MainFrame
###########################################################################

ERR_TOL = 1e-5  # floating point slop for peak-detection


matplotlib.rc('image', origin='lower')


class PlotPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        self.fig = Figure()
        self.canvas = FigureCanvasWxAgg(self, -1, self.fig)
        self.toolbar = Toolbar(self.canvas)  # matplotlib toolbar
        self.toolbar.Realize()
        # self.toolbar.set_active([0,1])

        # Now put all into a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)

        # This way of adding to sizer allows resizing
        sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        # Best to allow the toolbar to resize!
        sizer.Add(self.toolbar, 0, wx.GROW)
        self.SetSizer(sizer)
        self.Fit()

    def init_plot_array(self):
        ax = self.fig.add_subplot(111)

        x = np.arange(120.0) * 2 * np.pi / 60.0
        y = np.arange(100.0) * 2 * np.pi / 50.0
        self.x, self.y = np.meshgrid(x, y)
        z = np.sin(self.x) + np.cos(self.y)
        self.im = a.imshow(z, cmap=cm.jet)  # , interpolation='nearest')

        zmax = np.amax(z) - ERR_TOL
        ymax_i, xmax_i = np.nonzero(z >= zmax)
        if self.im.origin == 'upper':
            ymax_i = z.shape[0] - ymax_i
        self.lines = a.plot(xmax_i, ymax_i, 'ko')

        self.toolbar.update()  # Not sure why this is needed - ADS

    def init_plot(self,x,y,title='',xlabel='',ylabel=''):
        ax = self.fig.add_subplot(111)

        self.lines = ax.plot(x,y)

        self.toolbar.update()  # Not sure why this is needed - ADS


    
    def GetToolBar(self):
        # You will need to override GetToolBar if you are using an
        # unmanaged toolbar in your frame
        return self.toolbar

    def OnWhiz(self, evt):
        self.x += np.pi / 15
        self.y += np.pi / 20
        z = np.sin(self.x) + np.cos(self.y)
        self.im.set_array(z)

        zmax = np.amax(z) - ERR_TOL
        ymax_i, xmax_i = np.nonzero(z >= zmax)
        if self.im.origin == 'upper':
            ymax_i = z.shape[0] - ymax_i
        self.lines[0].set_data(xmax_i, ymax_i)

        self.canvas.draw()

    def onEraseBackground(self, evt):
        # this is supposed to prevent redraw flicker on some X servers...
        pass





class MainFrame ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
    
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Equations = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
        
        Equations = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self.Equations, wx.ID_ANY, u"Equations", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        Equations.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.eqnDisplay = wx.TextCtrl( self.Equations, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_MULTILINE|wx.TE_READONLY )
        Equations.Add( self.eqnDisplay, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        gSizer1.Add( Equations, 2, wx.EXPAND, 5 )
        
        Parameters = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText11 = wx.StaticText( self.Equations, wx.ID_ANY, u"Parameters", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        Parameters.Add( self.m_staticText11, 0, wx.ALL, 5 )
        
        self.paramDisplay = wx.TextCtrl( self.Equations, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        Parameters.Add( self.paramDisplay, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        gSizer1.Add( Parameters, 2, wx.EXPAND, 5 )
        
        Initial_Conditions = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText111 = wx.StaticText( self.Equations, wx.ID_ANY, u"Initial Conditions", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText111.Wrap( -1 )
        Initial_Conditions.Add( self.m_staticText111, 0, wx.ALL, 5 )
        
        self.initDisplay = wx.TextCtrl( self.Equations, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        Initial_Conditions.Add( self.initDisplay, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        gSizer1.Add( Initial_Conditions, 2, wx.EXPAND, 5 )
        
        Options = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1111 = wx.StaticText( self.Equations, wx.ID_ANY, u"Options", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1111.Wrap( -1 )
        Options.Add( self.m_staticText1111, 0, wx.ALL, 5 )
        
        self.optDisplay = wx.TextCtrl( self.Equations, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        Options.Add( self.optDisplay, 1, wx.ALL|wx.EXPAND, 5 )
        
        gSizer1.Add( Options, 2, wx.EXPAND, 5 )
        
        bSizer9 = wx.BoxSizer( wx.VERTICAL )
        
        self.filenameDisplay = wx.StaticText( self.Equations, wx.ID_ANY, u"No ODE file loaded.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.filenameDisplay.Wrap( -1 )
        bSizer9.Add( self.filenameDisplay, 0, wx.ALL, 5 )
        
        
        gSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )
        
        bSizer10 = wx.BoxSizer( wx.VERTICAL )


        self.openButton = wx.Button( self.Equations, wx.ID_ANY, u"Open...", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.openButton, 0, wx.ALL, 5 )

        
        self.saveButton = wx.Button( self.Equations, wx.ID_ANY, u"Save and Run", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.saveButton, 0, wx.ALL, 5 )


        
        gSizer1.Add( bSizer10, 1, wx.EXPAND, 5 )
        
        
        self.Equations.SetSizer( gSizer1 )
        self.Equations.Layout()
        gSizer1.Fit( self.Equations )
        self.m_notebook1.AddPage( self.Equations, u"Equations", True )



        self.Output = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        # text box for xpp output
        self.outDisplay = wx.TextCtrl( self.Output, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
        bSizer3.Add( self.outDisplay, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.Output.SetSizer( bSizer3 )
        self.Output.Layout()
        bSizer3.Fit( self.Output )
        self.m_notebook1.AddPage( self.Output, u"Output", False )



        self.Graphs = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_notebook1.AddPage( self.Graphs, u"Graphs", False )



        bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        
        filemenu= wx.Menu()
        
        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        menuOpen = filemenu.Append(wx.ID_OPEN,"Open...","Open an ODE file")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        
        
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        
        # Set events.
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)

        self.Bind(wx.EVT_BUTTON, self.RunAndSave, self.saveButton)
        self.Bind(wx.EVT_BUTTON, self.OnOpen, self.openButton)
        
        self.Show(True)


        # matplotlib panel
        self.plotpanel = PlotPanel(self.Graphs)



        self.fullname = ''
        
    def OnExit(self,e):
        self.Close(True)  # Close the frame.


    def OnOpen(self,e):
        """ Open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "ODE files (*.ode)|*.ode|All Files (*.*)|*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            self.fullname = os.path.join(self.dirname, self.filename)
            f = open(self.fullname, 'r')


            ## extract relevant information

            # read equations and display
            self.eqnDisplay.SetValue(f.read())

            
            # read parameters and display
            params = read_pars(self.fullname)
            paramslist = ''
            for i in params:
                paramslist += str(i)+'='+params[i]+'\n'
            
            self.paramDisplay.SetValue(paramslist)

            # read initial conditions and display
            inits = read_inits(self.fullname)
            initslist = ''
            for i in inits:
                initslist += str(i)+'='+inits[i]+'\n'
            
            self.initDisplay.SetValue(initslist)
            

            # read options and display
            opts = read_numerics(self.fullname)
            optslist = ''
            for i in opts:
                optslist += str(i)+'='+opts[i]+'\n'
            self.optDisplay.SetValue(optslist)


            # update filename
            self.filenameDisplay.SetLabel('Loaded '+self.filename)


            f.close()
        dlg.Destroy()
        
    

    def RunAndSave(self,e):
        try:
            print 'running xpp'
            self.npa, self.vn = xpprun(self.fullname, clean_after=True)
            self.t = self.npa[:,0]
            self.sv = self.npa[:,1:]

            # update graph
            self.plotpanel.init_plot(self.t,self.npa[:,1])

        except IOError:
            # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
            dlg = wx.MessageDialog( self, "Please load an ODE file first.", "Error", wx.OK)
            dlg.ShowModal() # Show it
            dlg.Destroy() # finally destroy it when finished.



    def __del__( self ):
        pass
	

ex = wx.App() 
MainFrame(None) 
ex.MainLoop()
